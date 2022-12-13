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
    data=khulshiGrid.objects.all()
    context = {
        'data':data,
    }
    pdf = render_to_pdf('data_pdf.html',context)
    if pdf:
        response = HttpResponse(pdf,content_type="application/pdf")
        content = "inline; filename=data.pdf"
        response['Content-Disposition']=content
        return response
    return HttpResponse("not found")
