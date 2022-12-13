from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from loadinput.models import khulshiGrid,HathazariGrid,HalishahorGrid,BakliaGrid,AgrabadGrid,RampurGrid ,SholoshahorGrid
from loadinput.models import KalurghatGrid,BarauliaGrid,ShahmirpurGrid,JuldaGrid, MadunaghatGrid,ChandroghunaGrid
from loadinput.models import DuhazariGrid,CoxBazarGrid,MatarbariGrid, KhagrachariGrid,RanghamatiGrid,BarairhatGrid
from loadinput.models import AKS132kvGrid ,KsrmGrid,MSMLGrid,SASMGrid, ShikalbhahaGrid,KaptaiGrid,TKGrid
from loadinput.models import ASK230KVGrid,BSRM230KVGrid,GPH230KVGrid,MirashoraiEZ
# Create your views here
@login_required
def dashboard_page(request):
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

    # sum data
    # sum = int(data_mad[0])+int(data_hat[0])+int(data_bak[0])
    context_data={
        'data_mad':data_mad,'data_hat':data_hat,'data_bak':data_bak, 'data_khul':data_khul,'data_hali':data_hali, 
        'data_agr':data_agr,'data_ramp':data_ramp,'data_sho':data_sho,'data_kalu':data_kalu, 'data_bar':data_bar,
        'data_sha':data_sha,'data_jul':data_jul,'data_chan':data_chan,'data_du':data_du,'data_cox':data_cox, 
        'data_mat':data_mat,'data_khag':data_khag,'data_rang':data_rang,'data_baraio':data_baraio,
        'data_aks132':data_aks132,'data_msml':data_msml,'data_ksrm':data_ksrm,'data_sasm':data_sasm,
        'data_shikl':data_shikl,'data_tk':data_tk,'data_kap':data_kap,'data_aks230':data_aks230,
        'data_bsrm230':data_bsrm230,'data_gph':data_gph,'data_mir':data_mir,
        # 'sum':sum,
    }
    return render(request, 'dashboard.html',context=context_data)


@login_required
def Home_page(request):
    return render(request, 'home.html')
