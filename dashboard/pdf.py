from io import BytesIO
from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse
from xhtml2pdf import pisa

from loadinput.models import khulshiGrid,HathazariGrid,HalishahorGrid,BakliaGrid,AgrabadGrid,RampurGrid ,SholoshahorGrid
from loadinput.models import KalurghatGrid,BarauliaGrid,ShahmirpurGrid,JuldaGrid, MadunaghatGrid,ChandroghunaGrid
from loadinput.models import DuhazariGrid,CoxBazarGrid,MatarbariGrid, KhagrachariGrid,RanghamatiGrid,BarairhatGrid
from loadinput.models import AKS132kvGrid ,KsrmGrid,MSMLGrid,SASMGrid, ShikalbhahaGrid,KaptaiGrid,TKGrid
from loadinput.models import ASK230KVGrid,BSRM230KVGrid,GPH230KVGrid,MirashoraiEZ

def render_to_pdf(template_src, context_dic={}):
    template = get_template(template_src)
    html = template.render(context_dic)
    result=BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")),result)
    if not pdf.err:
        return HttpResponse(result.getvalue(),content_type="application/pdf")
    return None
    
def data_pdf(request):
    data_mad = MadunaghatGrid.objects.all()
    data_hat = HathazariGrid.objects.all()
    data_bak = BakliaGrid.objects.all()
    data_khul = khulshiGrid.objects.all()
    data_hali = HalishahorGrid.objects.all()
    data_agr = AgrabadGrid.objects.all()
    data_ramp = RampurGrid.objects.all()
    data_sho = SholoshahorGrid.objects.all()
    data_kalu = KalurghatGrid.objects.all()
    data_bar = BarauliaGrid.objects.all()
    data_sha = ShahmirpurGrid.objects.all()
    data_jul = JuldaGrid.objects.all()
    data_chan = ChandroghunaGrid.objects.all()
    data_du = DuhazariGrid.objects.all()
    data_cox = CoxBazarGrid.objects.all()
    data_mat = MatarbariGrid.objects.all()
    data_khag = KhagrachariGrid.objects.all()
    data_rang = RanghamatiGrid.objects.all()
    data_baraio = BarairhatGrid.objects.all()
    data_aks132 = AKS132kvGrid.objects.all()
    data_msml = MSMLGrid.objects.all()
    data_ksrm = KsrmGrid.objects.all()
    data_sasm = SASMGrid.objects.all()
    data_shikl = ShikalbhahaGrid.objects.all()
    data_tk= TKGrid.objects.all()
    data_kap= KaptaiGrid.objects.all()
    data_aks230 = ASK230KVGrid.objects.all()
    data_bsrm230 = BSRM230KVGrid.objects.all()
    data_gph = GPH230KVGrid.objects.all()
    data_mir = MirashoraiEZ.objects.all()
    context = {
        'data':data_mad,'data':data_hat,'data':data_bak, 'data':data_khul,'data':data_hali, 
        'data':data_agr,'data':data_ramp,'data':data_sho,'data':data_kalu, 'data':data_bar,
        'data_sha':data_sha,'data_jul':data_jul,'data_chan':data_chan,'data_du':data_du,'data_cox':data_cox, 
        'data_mat':data_mat,'data_khag':data_khag,'data_rang':data_rang,'data_baraio':data_baraio,
        'data_aks132':data_aks132,'data_msml':data_msml,'data_ksrm':data_ksrm,'data_sasm':data_sasm,
        'data_shikl':data_shikl,'data_tk':data_tk,'data_kap':data_kap,'data_aks230':data_aks230,
        'data_bsrm230':data_bsrm230,'data_gph':data_gph,'data_mir':data_mir,
    }
    pdf = render_to_pdf('download.html',context)
    if pdf:
        response = HttpResponse(pdf,content_type="application/pdf")
        content = "inline; filename=data.pdf"
        response['Content-Disposition']=content
        return response
    return HttpResponse("not found")
