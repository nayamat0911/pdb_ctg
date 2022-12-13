from django import forms

from .models import khulshiGrid,HathazariGrid,HalishahorGrid,BakliaGrid,AgrabadGrid,RampurGrid, SholoshahorGrid
from .models import KalurghatGrid,BarauliaGrid,ShahmirpurGrid,JuldaGrid, MadunaghatGrid,ChandroghunaGrid
from .models import DuhazariGrid,CoxBazarGrid,MatarbariGrid, KhagrachariGrid,RanghamatiGrid,BarairhatGrid
from .models import AKS132kvGrid ,KsrmGrid,MSMLGrid,SASMGrid, ShikalbhahaGrid,KaptaiGrid,TKGrid

# 230 KV Load
from .models import ASK230KVGrid,BSRM230KVGrid,GPH230KVGrid,MirashoraiEZ

# reb 
from loadinput.models import Hathazari_REB,Baraulia_REB,Shahmirpur_REB, Julda_REB,Madunaghat_REB,Chandroghuna_REB
from loadinput.models import Duhazari_REB,CoxBazar_REB,Matarbari_REB,Barairhat_REB,Shikalbhaha_REB,TK_REB



class KhulshiGirdForm(forms.ModelForm):
    class Meta:
        model=khulshiGrid
        fields = '__all__'

class HathazariGridForm(forms.ModelForm):
    class Meta:
        model=HathazariGrid
        fields = '__all__'

class Hathazari_REB_Form(forms.ModelForm):#-----reb 
    class Meta:
        model=Hathazari_REB
        fields = '__all__'

class HalishahorGridForm(forms.ModelForm):
    class Meta:
        model=HalishahorGrid
        fields = '__all__'

class BakliaGridForm(forms.ModelForm):
    class Meta:
        model=BakliaGrid
        fields = '__all__'

class AgrabadGridForm(forms.ModelForm):
    class Meta:
        model=AgrabadGrid
        fields = '__all__'

class RampurGridForm(forms.ModelForm):
    class Meta:
        model=RampurGrid
        fields = '__all__'

class SholoshahorGridForm(forms.ModelForm):
    class Meta:
        model=SholoshahorGrid
        fields = '__all__'

class KalurghatGridForm(forms.ModelForm):
    class Meta:
        model=KalurghatGrid
        fields = '__all__'

class BarauliaGridForm(forms.ModelForm):
    class Meta:
        model=BarauliaGrid
        fields = '__all__'

class Baraulia_REB_Form(forms.ModelForm): #-----reb
    class Meta:
        model=Baraulia_REB
        fields = '__all__'

class ShahmirpurGridForm(forms.ModelForm):
    class Meta:
        model=ShahmirpurGrid
        fields = '__all__'

class Shahmirpur_REB_Form(forms.ModelForm):#-----reb
    class Meta:
        model=Shahmirpur_REB
        fields = '__all__'

class JuldaGridForm(forms.ModelForm):
    class Meta:
        model=JuldaGrid
        fields = '__all__'

class Julda_REB_Form(forms.ModelForm):
    class Meta:
        model=Julda_REB
        fields = '__all__'

class JuldaGridForm(forms.ModelForm):
    class Meta:
        model=JuldaGrid
        fields = '__all__'

class MadunaghatGridForm(forms.ModelForm):
    class Meta:
        model=MadunaghatGrid
        fields = '__all__'

class Madunaghat_REB_Form(forms.ModelForm): #----reb-------
    class Meta:
        model=Madunaghat_REB
        fields = '__all__'

class ChandroghunaGridForm(forms.ModelForm):
    class Meta:
        model=ChandroghunaGrid
        fields = '__all__'

class Chandroghuna_REB_Form(forms.ModelForm): #----reb-------
    class Meta:
        model=Chandroghuna_REB
        fields = "__all__"

class DuhazariGridForm(forms.ModelForm):
    class Meta:
        model=DuhazariGrid
        fields = '__all__'

class Duhazari_REB_Form(forms.ModelForm):#-----reb----
    class Meta:
        model=Duhazari_REB
        fields = '__all__'

class CoxsBazarGridForm(forms.ModelForm):
    class Meta:
        model=CoxBazarGrid
        fields = '__all__'

class CoxsBazar_REB_Form(forms.ModelForm): #-----reb----
    class Meta:
        model=CoxBazar_REB
        fields = '__all__'

class MatarbariGridForm(forms.ModelForm):
    class Meta:
        model=MatarbariGrid
        fields = '__all__'

class Matarbari_REB_Form(forms.ModelForm):#-----reb---
    class Meta:
        model=Matarbari_REB
        fields = '__all__'

class KhagrachariGridForm(forms.ModelForm):
    class Meta:
        model=KhagrachariGrid
        fields = '__all__'

class RanghamatiGridForm(forms.ModelForm):
    class Meta:
        model=RanghamatiGrid
        fields = '__all__'

class BarairhatGridForm(forms.ModelForm):
    class Meta:
        model=BarairhatGrid
        fields = '__all__'

class Barairhat_REB_Form(forms.ModelForm):#-----reb---
    class Meta:
        model=Barairhat_REB
        fields = '__all__'

class AKS132kvGridForm(forms.ModelForm):
    class Meta:
        model=AKS132kvGrid
        fields = '__all__'

class KsrmGridForm(forms.ModelForm):
    class Meta:
        model=KsrmGrid
        fields = '__all__'

class MSMLGridForm(forms.ModelForm):
    class Meta:
        model=MSMLGrid
        fields = '__all__'

class SASMGridForm(forms.ModelForm):
    class Meta:
        model=SASMGrid
        fields = '__all__'

class ShikalbhahaGridForm(forms.ModelForm):
    
    class Meta:
        model=ShikalbhahaGrid
        fields = '__all__'

class Shikalbhaha_REB_Form(forms.ModelForm):#-----reb---
    class Meta:
        model=Shikalbhaha_REB
        fields = '__all__'
        labels = {
        
        "Anowara": "anowara",
        "Boalkhali": "boalkhali",
        }
    #     widgets = {
    #     "Anowara": forms.intInput(attrs={'class':'form-control', "placeholder":"Anowara"}),
    #     "Boalkhali": forms.intInput(attrs={'class':'form-control', "placeholder":"Boalkhali"})
        
    # }


class KaptaiGridForm(forms.ModelForm):
    class Meta:
        model=KaptaiGrid
        fields = '__all__'

class TKGridForm(forms.ModelForm):
    class Meta:
        model=TKGrid
        fields = '__all__'

class TK_REB_Form(forms.ModelForm):#-----reb----
    class Meta:
        model=TK_REB
        fields = '__all__'


#------------------------------230 KV-------------------------------
class AKS230KVGridForm(forms.ModelForm):
    class Meta:
        model=ASK230KVGrid
        fields = '__all__'

class BSRM230KVGridForm(forms.ModelForm):
    class Meta:
        model=BSRM230KVGrid
        fields = '__all__'

class GPH230KVGridForm(forms.ModelForm):
    class Meta:
        model=GPH230KVGrid
        fields = '__all__'

class MirashoraiEZGridForm(forms.ModelForm):
    class Meta:
        model=MirashoraiEZ
        fields = '__all__'





# ---------old--------





