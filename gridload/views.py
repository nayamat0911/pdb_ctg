from django.shortcuts import render
from gridload import forms
from .models import GridLoad,PDBShed,REBShed
from .forms import GirdLoadForm, PDBShedForm,REBShedForm
from django.contrib.auth.decorators import login_required

from loadinput.models import khulshiGrid,HathazariGrid,HalishahorGrid,BakliaGrid,AgrabadGrid,RampurGrid ,SholoshahorGrid
from loadinput.models import KalurghatGrid,BarauliaGrid,ShahmirpurGrid,JuldaGrid, MadunaghatGrid,ChandroghunaGrid
from loadinput.models import DuhazariGrid,CoxBazarGrid,MatarbariGrid, KhagrachariGrid,RanghamatiGrid,BarairhatGrid
from loadinput.models import AKS132kvGrid ,KsrmGrid,MSMLGrid,SASMGrid, ShikalbhahaGrid,KaptaiGrid,TKGrid
from loadinput.models import ASK230KVGrid,BSRM230KVGrid,GPH230KVGrid,MirashoraiEZ

# for reb 
# reb 
from loadinput.models import Hathazari_REB,Baraulia_REB,Shahmirpur_REB,Julda_REB, Madunaghat_REB,Chandroghuna_REB
from loadinput.models import Duhazari_REB,CoxBazar_REB,Matarbari_REB,Barairhat_REB,Shikalbhaha_REB,TK_REB

# Create your views here

    
    
# ----------------------------------Grid load Show---------------------
@login_required
def Grid_load_show(request):
    
    return render(request, 'gridload_show.html')

# ----------------------------------Grid load input---------------------
@login_required
def Grid_load_input(request):
    form1 = forms.GirdLoadForm()
    form2 = forms.PDBShedForm()
    form3 = forms.REBShedForm()
    context_form = {
        'form1':form1,
        'form2':form2,
        'form3':form3,
    }
    return render(request, 'gridload_user.html', context=context_form)

# ----------------------------------PDB REB---------------------
@login_required
def PDB_RRB(request):
    context_pdb_reb = {
        'title_name':'PDB & REB LOAD',
        
    }
    return render(request, 'pdb_reb.html', context=context_pdb_reb)


# ----------------------------------PDB REB SHED---------------------
@login_required
def PDB_RRB_shed(request):
    shed_pdb=HathazariGrid.objects.all()
    context_pdb_reb_shed = {
        'title_name':'PDB & REB LOAD SHED',
        'shed_pdb':shed_pdb,
    }
    return render(request, 'pdb_reb_shed.html', context=context_pdb_reb_shed)


# ----------------------------------REB LOAD---------------------
@login_required
def REB_load(request):
    data_mad = Madunaghat_REB.objects.all()
    data_hat = Hathazari_REB.objects.all()
    data_bar = Baraulia_REB.objects.all()
    data_sha = Shahmirpur_REB.objects.all()
    data_jul = Julda_REB.objects.all()
    data_chan = Chandroghuna_REB.objects.all()
    data_du = Duhazari_REB.objects.all()
    data_cox = CoxBazar_REB.objects.all()
    data_mat = Matarbari_REB.objects.all()
    data_baraio = Barairhat_REB.objects.all()
    data_shikl = Shikalbhaha_REB.objects.all()
    # data_tk= TK_REB.objects.all()
    data_mir = MirashoraiEZ.objects.all()

    # sum data
    # sum = int(data_mad[0])+int(data_hat[0])+int(data_bak[0])
    context_reb_load={
        'data_mad':data_mad,'data_hat':data_hat, 'data_bar':data_bar,'data_sha':data_sha,
        'data_jul':data_jul,'data_chan':data_chan,'data_du':data_du,'data_cox':data_cox, 
        'data_mat':data_mat,'data_baraio':data_baraio,'data_shikl':data_shikl,
        # 'data_tk':data_tk,'data_mir':data_mir,
        # 'sum':sum,
    }
    return render(request, 'reb_load.html', context=context_reb_load)


