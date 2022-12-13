from django.shortcuts import render,redirect

# important and common import here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import datetime
# download-------- 
from io import BytesIO
from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse
# for khulshi grid
# -------------------------from models----------------------
from .models import khulshiGrid,HathazariGrid,HalishahorGrid,BakliaGrid,AgrabadGrid,RampurGrid ,SholoshahorGrid
from .models import KalurghatGrid,BarauliaGrid,ShahmirpurGrid,JuldaGrid, MadunaghatGrid,ChandroghunaGrid
from .models import DuhazariGrid,CoxBazarGrid,MatarbariGrid, KhagrachariGrid,RanghamatiGrid,BarairhatGrid
from .models import AKS132kvGrid ,KsrmGrid,MSMLGrid,SASMGrid, ShikalbhahaGrid,KaptaiGrid,TKGrid
from .models import ASK230KVGrid,BSRM230KVGrid,GPH230KVGrid,MirashoraiEZ

# for reb 
# reb 
from loadinput.models import Hathazari_REB,Baraulia_REB,Shahmirpur_REB,Julda_REB, Madunaghat_REB,Chandroghuna_REB
from loadinput.models import Duhazari_REB,CoxBazar_REB,Matarbari_REB,Barairhat_REB,Shikalbhaha_REB,TK_REB

# ---------------------froms--------------
from loadinput.forms import KhulshiGirdForm,HathazariGridForm,HalishahorGridForm,BakliaGridForm, AgrabadGridForm,RampurGridForm,SholoshahorGridForm
from loadinput.forms import KalurghatGridForm, BarauliaGridForm,ShahmirpurGridForm,JuldaGridForm, MadunaghatGridForm,ChandroghunaGridForm
from loadinput.forms import DuhazariGridForm,CoxsBazarGridForm,MatarbariGridForm,KhagrachariGridForm,RanghamatiGridForm,BarairhatGridForm
from loadinput.forms import AKS132kvGridForm,KsrmGridForm,MSMLGridForm,SASMGridForm,ShikalbhahaGridForm,KaptaiGridForm,TKGridForm
from loadinput.forms import AKS230KVGridForm,BSRM230KVGridForm,GPH230KVGridForm,MirashoraiEZGridForm

# for reb
from loadinput.forms import Hathazari_REB_Form, Baraulia_REB_Form,Shahmirpur_REB_Form,Julda_REB_Form, Madunaghat_REB_Form,Chandroghuna_REB_Form
from loadinput.forms import Duhazari_REB_Form,CoxsBazar_REB_Form,Matarbari_REB_Form,Barairhat_REB_Form,Shikalbhaha_REB_Form,TK_REB_Form

# Create your views here


@login_required  #--------------------------------khulshi-----------------
def Khulshi(request):
    data = khulshiGrid.objects.all()      
    if request.method == "POST":
        form = KhulshiGirdForm(request.POST)        
        if form.is_valid():
            form.save()
            return redirect ('loadinput:Khulshi')
    else:    
        form = KhulshiGirdForm()        
    khulshi_load = {
        'title_name':'Khulshi 132/33 KV Grid Substation ',
        'g__khul':form,
        'load__kkul':data,
    }
    return render(request, 'grid/khulshi.html', context=khulshi_load)


def Hathazari(request): #------------------Hathazari-------------------------
    load = HathazariGrid.objects.all()
    if request.method == "POST":
        gridForm = HathazariGridForm(request.POST)
        if gridForm.is_valid():
            gridForm.save()
            return redirect ('loadinput:hathazari')
    else:
        gridForm = HathazariGridForm()

    Hathazari_load = {
        'title_name':'Hathazari 230/132/33 KV Grid Substation ',
        'g__hat':gridForm,
        'load__hat':load,
    
    }
    return render(request, 'grid/hathazari.html', context=Hathazari_load) 

def Hathazari__REB(request): #------------------REB-------------------------
    load_reb = Hathazari_REB.objects.all()
    if request.method == "POST":
        rebForm = Hathazari_REB_Form(request.POST)
        if rebForm.is_valid():
            rebForm.save()
            return redirect ('loadinput:hathazari__reb')
    else:
        rebForm = Hathazari_REB_Form()

    Hathazari_load_reb = {
        'title_name':'Hathazari 230/132/33 KV Grid Substation REB LOAD ',
        'g__hat__reb':rebForm,
        'load__hat__reb':load_reb,
    
    }
    return render(request, 'reb/hathazari_reb.html', context=Hathazari_load_reb)

def Halishohor(request): #-----------------------halishahor-------------------------
    load = HalishahorGrid.objects.all()
    if request.method == "POST":
        gridForm = HalishahorGridForm(request.POST)
        if gridForm.is_valid():
            gridForm.save()
            return redirect ('loadinput:halishahor')
    else:
        gridForm = HalishahorGridForm()

    Halishahor_load = {
        'title_name':'Halishahor Grid 132/33 KV Substation ',
        'g__hali':gridForm,
        'load__hali':load
    
    }
    return render(request, 'grid/halishahor.html', context=Halishahor_load)

def BakliaLoad(request): #-----------------------------------bakalia grid ---------------------------
    load = BakliaGrid.objects.all()
    if request.method == "POST":
        gridForm = BakliaGridForm(request.POST)
        if gridForm.is_valid():
            gridForm.save()
            return redirect ('loadinput:Bakalia')
    else:
        gridForm = BakliaGridForm()

    Baklia_load = {
        'title_name':'Baklia 132/33 KV Grid Substation ',
        'g__bako':gridForm,
        'load__bako':load
    
    }
    return render(request, 'grid/bakalia.html', context=Baklia_load)

def Agrabad(request): #-----------------------------------Agrabad grid ---------------------------
    load = AgrabadGrid.objects.all()
    if request.method == "POST":
        gridForm = AgrabadGridForm(request.POST)
        if gridForm.is_valid():
            gridForm.save()
            return redirect ('loadinput:agrabad')
    else:
        gridForm = AgrabadGridForm()

    Agrabad_load = {
        'title_name':'Agrabad 132/33 KV Grid Substation ',
        'g__agr':gridForm,
        'load__agr':load
    
    }
    return render(request, 'grid/agrabad.html', context=Agrabad_load)

def Rampur(request): #-----------------------------------Rampur grid ---------------------------
    load = RampurGrid.objects.all()
    if request.method == "POST":
        gridForm = RampurGridForm(request.POST)
        if gridForm.is_valid():
            gridForm.save()
            return redirect ('loadinput:rampur')
    else:
        gridForm = RampurGridForm()

    Rampur_load = {
        'title_name':'Rampur 132/33 KV Grid Substation ',
        'g__ramp':gridForm,
        'load__ramp':load
    
    }
    return render(request, 'grid/rampur.html', context=Rampur_load)

def Sholoshahor(request): #-----------------------------------Sholoshahor grid ---------------------------
    load = SholoshahorGrid.objects.all()
    if request.method == "POST":
        gridForm = SholoshahorGridForm(request.POST)
        if gridForm.is_valid():
            gridForm.save()
            return redirect ('loadinput:sholoshahor')
    else:
        gridForm = SholoshahorGridForm()

    Sholoshahor_load = {
        'title_name':'Sholoshahor 132/33 KV Grid Substation ',
        'g__sho':gridForm,
        'load__sho':load
    }
    return render(request, 'grid/sholoshahor.html', context=Sholoshahor_load)


def Kalurghat(request): #-----------------------------------Kalurghat grid ---------------------------
    load = KalurghatGrid.objects.all()
    if request.method == "POST":
        gridForm = KalurghatGridForm(request.POST)
        if gridForm.is_valid():
            gridForm.save()
            return redirect ('loadinput:kalurghat')
    else:
        gridForm = KalurghatGridForm()

    Kalurghat_load = {
        'title_name':'Kalurghat 132/33 KV Grid Substation ',
        'g__kalu':gridForm,
        'load__kalu':load
    }
    return render(request, 'grid/kalurghat.html', context=Kalurghat_load)


def Barulia(request): #-----------------------------------Barulia grid ---------------------------
    load = BarauliaGrid.objects.all()
    if request.method == "POST":
        gridForm = BarauliaGridForm(request.POST)
        if gridForm.is_valid():
            gridForm.save()
            return redirect ('loadinput:barulia')
    else:
        gridForm = BarauliaGridForm()

    Barulia_load = {
        'title_name':'Barulia 132/33 KV Grid Substation ',
        'g__bar':gridForm,
        'load__bar':load
    }
    return render(request, 'grid/baraulia.html', context=Barulia_load)

def Barulia__REB(request): #--------------------------------REB ---------------------------
    load_reb = Baraulia_REB.objects.all()
    if request.method == "POST":
        rebForm = Baraulia_REB_Form(request.POST)
        if rebForm.is_valid():
            rebForm.save()
            return redirect ('loadinput:barulia__reb')
    else:
        rebForm = Baraulia_REB_Form()

    Barulia_load_reb = {
        'title_name':'Barulia 132/33 KV Grid Substation REB LOAD',
        'g__bar_reb':rebForm,
        'load__bar_reb':load_reb
    }
    return render(request, 'reb/baroulia_reb.html', context=Barulia_load_reb)


def Shahmirpur(request): #-----------------------------------Shahmirpur grid ---------------------------
    load = ShahmirpurGrid.objects.all()
    if request.method == "POST":
        gridForm = ShahmirpurGridForm(request.POST)
        if gridForm.is_valid():
            gridForm.save()
            return redirect ('loadinput:shahmirpur')
    else:
        gridForm = ShahmirpurGridForm()

    Shahmirpur_load = {
        'title_name':'Shahmirpur 132/33 KV Grid Substation ',
        'g__sha':gridForm,
        'load__sha':load
    }
    return render(request, 'grid/shahmirpur.html', context=Shahmirpur_load)

def Shahmirpur__REB(request): #---------------------------REB ---------------------------
    load_reb = Shahmirpur_REB.objects.all()
    if request.method == "POST":
        rebForm = Shahmirpur_REB_Form(request.POST)
        if rebForm.is_valid():
            rebForm.save()
            return redirect ('loadinput:shahmirpur__reb')
    else:
        rebForm = Shahmirpur_REB_Form()

    Shahmirpur_load_reb = {
        'title_name':'Shahmirpur 132/33 KV Grid Substation REB LOAD',
        'g__sha_reb':rebForm,
        'load__sha_reb':load_reb
    }
    return render(request, 'reb/shahmirpur_reb.html', context=Shahmirpur_load_reb)

def Julda(request): #-----------------------------------Julda grid ---------------------------
    load = JuldaGrid.objects.all()
    if request.method == "POST":
        gridForm = JuldaGridForm(request.POST)
        if gridForm.is_valid():
            gridForm.save()
            return redirect ('loadinput:julda')
    else:
        gridForm = JuldaGridForm()

    Julda_load = {
        'title_name':'Julda 132/33 KV Grid Substation ',
        'g__jul':gridForm,
        'load__jul':load
    }
    return render(request, 'grid/julda.html', context=Julda_load)

def Julda__REB(request): #-----------------------------------Julda grid ---------------------------
    load = Julda_REB.objects.all()
    if request.method == "POST":
        rebForm = Julda_REB_Form(request.POST)
        if rebForm.is_valid():
            rebForm.save()
            return redirect ('loadinput:julda__reb')
    else:
        rebForm = Julda_REB_Form()

    Julda_load = {
        'title_name':'Julda 132/33 KV Grid Substation REB LOAD',
        'g__jul_reb':rebForm,
        'load__jul_reb':load
    }
    return render(request, 'reb/julda_reb.html', context=Julda_load)


def Madunaghat(request): #------------------------------madunaghat grid -----------------------
    load = MadunaghatGrid.objects.all()
    if request.method == "POST":
        gridForm = MadunaghatGridForm(request.POST)
        if gridForm.is_valid():
            gridForm.save()
            return redirect ('loadinput:madunaaghat')
    else:
        gridForm = MadunaghatGridForm()
    madunaghat_load = {
        'title_name':'Madunaghat 132/33 KV Grid Substation ',
        'g__madu':gridForm,
        'load__madu':load    
    }
    return render(request, 'grid/madunaghat.html', context=madunaghat_load)


def Madunaghat__REB(request): #----------------------------- REB -----------------------
    load_reb = Madunaghat_REB.objects.all()
    if request.method == "POST":
        rebForm = Madunaghat_REB_Form(request.POST)
        if rebForm.is_valid():
            rebForm.save()
            return redirect ('loadinput:madunaaghat__reb')
    else:
        rebForm = Madunaghat_REB_Form()
    madunaghat_reb_load = {
        'title_name':'Madunaghat 132/33 KV Grid Substation REB LOAD',
        'g__madu_reb':rebForm,
        'load__madu_reb':load_reb    
    }
    return render(request, 'reb/madunaaghat_reb.html', context=madunaghat_reb_load)


def Chandroghuna(request): #-----------------------------------chandroghuna grid ---------------------------
    load = ChandroghunaGrid.objects.all()
    if request.method == "POST":
        gridForm = ChandroghunaGridForm(request.POST)
        if gridForm.is_valid():
            gridForm.save()
            return redirect ('loadinput:chandroghuna')
    else:
        gridForm = ChandroghunaGridForm()
    Chandroghuna_load = {
        'title_name':'Chandroghuna 132/33 KV Grid Substation ',
        'g__ch':gridForm,
        'load__ch':load
    }
    return render(request, 'grid/chondroghuna.html', context=Chandroghuna_load)

def Chandroghuna__REB(request): #---------------------------REB ---------------------------
    load_reb = Chandroghuna_REB.objects.all()
    if request.method == "POST":
        rebForm = Chandroghuna_REB_Form(request.POST)
        if rebForm.is_valid():
            rebForm.save()
            return redirect ('loadinput:chandroghuna__reb')
    else:
        rebForm = Chandroghuna_REB_Form()
    Chandroghuna_REB_load = {
        'title_name':'Chandroghuna 132/33 KV Grid Substation REB LOAD',
        'g__ch_reb':rebForm,
        'load__ch_reb':load_reb
    }
    return render(request, 'reb/chondroghuna_reb.html', context=Chandroghuna_REB_load)


def Duhazari(request): #-----------------------------------duhazari grid ---------------------------
    load = DuhazariGrid.objects.all()
    if request.method == "POST":
        gridForm = DuhazariGridForm(request.POST)
        if gridForm.is_valid():
            gridForm.save()
            return redirect ('loadinput:duhazari')
    else:
        gridForm = DuhazariGridForm()
    Duhazari_load = {
        'title_name':'Duhazari 132/33 KV Grid Substation ',
        'g__du':gridForm,
        'load__du':load
    }
    return render(request, 'grid/duhazari.html', context=Duhazari_load)

def Duhazari___REB(request): #-------------------------------REB  ---------------------------
    load_reb = Duhazari_REB.objects.all()
    if request.method == "POST":
        rebForm = Duhazari_REB_Form(request.POST)
        if rebForm.is_valid():
            rebForm.save()
            return redirect ('loadinput:duhazari__reb')
    else:
        rebForm = Duhazari_REB_Form()
    Duhazari_load_reb = {
        'title_name':'Duhazari 132/33 KV Grid Substation REB LOAD',
        'g__du_reb':rebForm,
        'load__du_reb':load_reb
    }
    return render(request, 'reb/duhazari_reb.html', context=Duhazari_load_reb)


def CoxBazar(request): #-----------------------------------coxbazar grid ---------------------------
    load = CoxBazarGrid.objects.all()
    if request.method == "POST":
        gridForm = CoxsBazarGridForm(request.POST)
        if gridForm.is_valid():
            gridForm.save()
            return redirect ('loadinput:coxsbazar')
    else:
        gridForm = CoxsBazarGridForm()
    CoxBazar_load = {
        'title_name':"Cox's-Bazar 132/33 KV Grid Substation",
        'g__cox':gridForm,
        'load__cox':load
    }
    return render(request, 'grid/coxsbazar.html', context=CoxBazar_load)

def CoxBazar__REB(request): #----------------------REB ---------------------------
    load_reb = CoxBazar_REB.objects.all()
    if request.method == "POST":
        rebForm = CoxsBazar_REB_Form(request.POST)
        if rebForm.is_valid():
            rebForm.save()
            return redirect ('loadinput:coxsbazar__reb')
    else:
        rebForm = CoxsBazar_REB_Form()
    CoxBazar_load_reb = {
        'title_name':"Cox's-Bazar 132/33 KV Grid Substation REB LOAD",
        'g__cox_reb':rebForm,
        'load__cox_reb':load_reb
    }
    return render(request, 'reb/coxbazar_reb.html', context=CoxBazar_load_reb)


def Matarbari(request): #-----------------------------------matarbari grid ---------------------------
    load = MatarbariGrid.objects.all()
    if request.method == "POST":
        gridForm = MatarbariGridForm(request.POST)
        if gridForm.is_valid():
            gridForm.save()
            return redirect ('loadinput:matarbari')
    else:
        gridForm = MatarbariGridForm()
    Matarbari_load = {
        'title_name':'Matarbari 132/33 KV Grid Substation ',
        'g__mat':gridForm,
        'load__mat':load
    }
    return render(request, 'grid/matarbari.html', context=Matarbari_load)

def Matarbari__REB(request): #--------------------------REB ---------------------------
    load_reb = Matarbari_REB.objects.all()
    if request.method == "POST":
        rebForm = Matarbari_REB_Form(request.POST)
        if rebForm.is_valid():
            rebForm.save()
            return redirect ('loadinput:matarbari__reb')
    else:
        rebForm = Matarbari_REB_Form()
    Matarbari_load_reb = {
        'title_name':'Matarbari 132/33 KV Grid Substation REB LOAD',
        'g__mat_reb':rebForm,
        'load__mat_reb':load_reb
    }
    return render(request, 'reb/matarbari_reb.html', context=Matarbari_load_reb)


def Khagrachari(request): #-----------------------------------Khagrachari grid ---------------------------
    load = KhagrachariGrid.objects.all()
    if request.method == "POST":
        gridForm = KhagrachariGridForm(request.POST)
        if gridForm.is_valid():
            gridForm.save()
            return redirect ('loadinput:khagrachari')
    else:
        gridForm = KhagrachariGridForm()

    Khagrachari_load = {
        'title_name':'Khagrachari 132/33 KV Grid Substation ',
        'g__khag':gridForm,
        'load__khag':load
    
    }
    return render(request, 'grid/khagrachari.html', context=Khagrachari_load)


def Ranghamati(request): #-----------------------------------Ranghamati grid ---------------------------
    load = RanghamatiGrid.objects.all()
    if request.method == "POST":
        gridForm = RanghamatiGridForm(request.POST)
        if gridForm.is_valid():
            gridForm.save()
            return redirect ('loadinput:ranghamati')
    else:
        gridForm = RanghamatiGridForm()

    Ranghamati_load = {
        'title_name':'Ranghamati 132/33 KV Grid Substation ',
        'g__rang':gridForm,
        'load__rang':load
    
    }
    return render(request, 'grid/ranghamati.html', context=Ranghamati_load)


def Baroiarhat(request): #-----------------------------------Barairhat grid ---------------------------
    load = BarairhatGrid.objects.all()
    if request.method == "POST":
        gridForm = BarairhatGridForm(request.POST)
        if gridForm.is_valid():
            gridForm.save()
            return redirect ('loadinput:baroiarhat')
    else:
        gridForm = BarairhatGridForm()
    Barairhat_load = {
        'title_name':"Baroiarhat 132/33 KV Grid Substation ",
        'g__bh':gridForm,
        'load__bh':load
    }
    return render(request, 'grid/baroiarhat.html', context=Barairhat_load)

def Baroiarhat__REB(request): #----------------------------REB ---------------------------
    load_reb = Barairhat_REB.objects.all()
    if request.method == "POST":
        rebForm = Barairhat_REB_Form(request.POST)
        if rebForm.is_valid():
            rebForm.save()
            return redirect ('loadinput:baroiarhat__reb')
    else:
        rebForm = Barairhat_REB_Form()
    Barairhat_load_reb = {
        'title_name':"Baroiarhat 132/33 KV Grid Substation REB LOAD",
        'g__bh_reb':rebForm,
        'load__bh_reb':load_reb
    }
    return render(request, 'reb/baroiarhat_reb.html', context=Barairhat_load_reb)


def AKS132kv(request): #-----------------------------------AKS132kv grid ---------------------------
    load = AKS132kvGrid.objects.all()
    if request.method == "POST":
        gridForm = AKS132kvGridForm(request.POST)
        if gridForm.is_valid():
            gridForm.save()
            return redirect ('loadinput:AKS132kv')
    else:
        gridForm = AKS132kvGridForm()
    AKS132kv_load = {
        'title_name':'AKS132kv 132/33 KV Grid Substation ',
        'g__aks132':gridForm,
        'load__aks132':load
    }
    return render(request, 'grid/AKS132kv.html', context=AKS132kv_load)

def Krsm(request): #-----------------------------------Krsm grid ---------------------------
    load = KsrmGrid.objects.all()
    if request.method == "POST":
        gridForm = KsrmGridForm(request.POST)
        if gridForm.is_valid():
            gridForm.save()
            return redirect ('loadinput:krsm')
    else:
        gridForm = KsrmGridForm()
    Krsm_load = {
        'title_name':'KRSM 132/33 KV Grid Substation ',
        'g__krsm':gridForm,
        'load__krsm':load
    }
    return render(request, 'grid/krsm.html', context=Krsm_load)

def MSML(request): #-----------------------------------MSML grid ---------------------------
    load = MSMLGrid.objects.all()
    if request.method == "POST":
        gridForm = MSMLGridForm(request.POST)
        if gridForm.is_valid():
            gridForm.save()
            return redirect ('loadinput:msml')
    else:
        gridForm = MSMLGridForm()
    MSML_load = {
        'title_name':'MSML 132/33 KV Grid Substation ',
        'g__msml':gridForm,
        'load__msml':load
    }
    return render(request, 'grid/msml.html', context=MSML_load)



def SASM(request): #-----------------------------------SASM grid ---------------------------
    load = SASMGrid.objects.all()
    if request.method == "POST":
        gridForm = SASMGridForm(request.POST)
        if gridForm.is_valid():
            gridForm.save()
            return redirect ('loadinput:sasm')
    else:
        gridForm = SASMGridForm()
    SASM_load = {
        'title_name':'SASM 132/33 KV Grid Substation ',
        'g__sasm':gridForm,
        'load__sasm':load
    }
    return render(request, 'grid/sasm132kv.html', context=SASM_load)


def Shikalbhaha(request): #-----------------------------------shikalbaha grid ---------------------------
    load = ShikalbhahaGrid.objects.all()
    if request.method == "POST":
        gridForm = ShikalbhahaGridForm(request.POST)
        if gridForm.is_valid():
            gridForm.save()
            return redirect ('loadinput:shikalbhaha')
    else:
        gridForm = ShikalbhahaGridForm()
    Shikalbhaha_load = {
        'title_name':'Shikalbhaha 132/33 KV Grid Substation ',
        'g__shikl':gridForm,
        'load__shikl':load
    }
    return render(request, 'grid/shikalbhaha.html', context=Shikalbhaha_load)

def Shikalbhaha__REB(request): #--------------------------REB ---------------------------
    load_reb = Shikalbhaha_REB.objects.all()
    if request.method == "POST":
        rebForm = Shikalbhaha_REB_Form(request.POST)
        if rebForm.is_valid():
            rebForm.save()
            return redirect ('loadinput:shikalbhaha__reb')
    else:
        rebForm = Shikalbhaha_REB_Form()
    Shikalbhaha_load_reb = {
        'title_name':'Shikalbhaha 132/33 KV Grid Substation REB LOAD',
        'g__shikl_reb':rebForm,
        'load__shikl_reb':load_reb
    }
    return render(request, 'reb/shikalbaha_reb.html', context=Shikalbhaha_load_reb)


def Kaptai(request): #-----------------------------------Kaptai grid ---------------------------
    load = KaptaiGrid.objects.all()
    if request.method == "POST":
        gridForm = KaptaiGridForm(request.POST)
        if gridForm.is_valid():
            gridForm.save()
            return redirect ('loadinput:kaptai')
    else:
        gridForm = KaptaiGridForm()
    Kaptai_load = {
        'title_name':'Kaptai 33/11 KV Grid Substation ',
        'g__kaptai':gridForm,
        'load__kaptai':load
    }
    return render(request, 'grid/kaptai.html', context=Kaptai_load)


def TK(request): #-----------------------------------TK grid ---------------------------
    load = TKGrid.objects.all()
    if request.method == "POST":
        gridForm = TKGridForm(request.POST)
        if gridForm.is_valid():
            gridForm.save()
            return redirect ('loadinput:tk132')
    else:
        gridForm = TKGridForm()
    TK_load = {
        'title_name':'TK 132/33 KV Grid Substation ',
        'g__tk':gridForm,
        'load__tk':load
    }
    return render(request, 'grid/tk132kv.html', context=TK_load)


def TK__REB(request): #----------------------------REB ---------------------------
    load_reb = TK_REB.objects.all()
    if request.method == "POST":
        rebForm = TK_REB_Form(request.POST)
        if rebForm.is_valid():
            rebForm.save()
            return redirect ('loadinput:tk132__reb')
    else:
        rebForm = TK_REB_Form()
    TK_load_reb = {
        'title_name':'TK 132/33 KV Grid Substation REB LOAD',
        'g__tk_reb':rebForm,
        'load__tk_reb':load_reb
    }
    return render(request, 'reb/tk_reb.html', context=TK_load_reb)

def AKS230KV(request): #-----------------------------------AKS 230 KV grid ---------------------------
    load = ASK230KVGrid.objects.all()
    if request.method == "POST":
        gridForm = AKS230KVGridForm(request.POST)
        if gridForm.is_valid():
            gridForm.save()
            return redirect ('loadinput:aks230kv')
    else:
        gridForm = AKS230KVGridForm()
    AKS_load = {
        'title_name':'Abul khayer 230/132/33 KV Grid Substation ',
        'g__aks230':gridForm,
        'load__aks230':load
    }
    return render(request, 'grid/aks230kv.html', context=AKS_load)

def BRSM230KV(request): #-----------------------------------BSRM 230 KV grid ---------------------------
    load = BSRM230KVGrid.objects.all()
    if request.method == "POST":
        gridForm = BSRM230KVGridForm(request.POST)
        if gridForm.is_valid():
            gridForm.save()
            return redirect ('loadinput:bsrm230kv')
    else:
        gridForm = BSRM230KVGridForm()
    BSRM_load = {
        'title_name':'BSRM 230/132/33 KV Grid Substation ',
        'g__bsrm230':gridForm,
        'load__bsrm230':load
    }
    return render(request, 'grid/bsrm230kv.html', context=BSRM_load)

def GPH230KV(request): #-----------------------------------GPH 230 KV grid ---------------------------
    load = GPH230KVGrid.objects.all()
    if request.method == "POST":
        gridForm = GPH230KVGridForm(request.POST)
        if gridForm.is_valid():
            gridForm.save()
            return redirect ('loadinput:gph230kv')
    else:
        gridForm = GPH230KVGridForm()
    GPH_load = {
        'title_name':'GPH 230/132/33 KV Grid Substation ',
        'g__gph230':gridForm,
        'load__gph230':load
    }
    return render(request, 'grid/gph230kv.html', context=GPH_load)

def Mirashorai(request): #-----------------------------------Mirashorai 230 KV grid ---------------------------
    load = MirashoraiEZ.objects.all()
    if request.method == "POST":
        gridForm = MirashoraiEZGridForm(request.POST)
        if gridForm.is_valid():
            gridForm.save()
            return redirect ('loadinput:mirashorai')
    else:
        gridForm = MirashoraiEZGridForm()
    Mirashorai_load = {
        'title_name':'Mirashorai EZ 230/132/33 KV Grid Substation ',
        'g__Mirashorai':gridForm,
        'load__Mirashorai':load
    }
    return render(request, 'grid/mirashorai.html', context=Mirashorai_load)









