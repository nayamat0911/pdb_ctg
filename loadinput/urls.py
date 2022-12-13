from django.urls import path
from . import views
#pdf
from .pdf import data_pdf 

app_name="loadinput"

urlpatterns = [
    #pdf
    path('pdf/', data_pdf, name='pdf'),
    
    #grid load------------------------------------------------
    path('khulshi/', views.Khulshi, name='Khulshi'),
    path('hathazari/', views.Hathazari, name='hathazari'),
    path('halishahor/', views.Halishohor, name='halishahor'),
    path('Bakalia/', views.BakliaLoad, name='Bakalia'),

    path('agrabd/', views.Agrabad, name='agrabad'),
    path('rampur/', views.Rampur, name='rampur'),
    path('sholoshahor/', views.Sholoshahor, name='sholoshahor'),

    path('kalurghat/', views.Kalurghat, name='kalurghat'),
    path('barulia/', views.Barulia, name='barulia'),

    path('shahmirpur/', views.Shahmirpur, name='shahmirpur'),
    path('julda/', views.Julda, name='julda'),

    path('madunaaghat/', views.Madunaghat, name='madunaaghat'),
    path('chandroghuna/', views.Chandroghuna, name='chandroghuna'),

    path('duhazari/', views.Duhazari, name='duhazari'),
    path('coxsbazar/', views.CoxBazar, name='coxsbazar'),
    path('matarbari/', views.Matarbari, name='matarbari'),

    path('khagrachari/', views.Khagrachari, name='khagrachari'),
    path('ranghamati/', views.Ranghamati, name='ranghamati'),
    path('baroiarhat/', views.Baroiarhat, name='baroiarhat'),

    path('aks132kv/', views.AKS132kv, name='AKS132kv'),
    path('krsm/', views.Krsm, name='krsm'),
    path('msml/', views.MSML, name='msml'),
    path('sasm/', views.SASM, name='sasm'),
    
    path('shikalbhaha/', views.Shikalbhaha, name='shikalbhaha'),
    path('kaptai/', views.Kaptai, name='kaptai'),
    path('tk132/', views.TK, name='tk132'),

    # 230 KV grid
    path('aks230kv/', views.AKS230KV, name='aks230kv'),
    path('bsrm230kv/', views.BRSM230KV, name='bsrm230kv'),
    path('gph230kv/', views.GPH230KV, name='gph230kv'),
    path('mirashoraiez/', views.Mirashorai, name='mirashorai'),
    

    #REB
    path('hathazari__reb/', views.Hathazari__REB, name='hathazari__reb'),
    path('barulia__reb/', views.Barulia__REB, name='barulia__reb'),
    path('shahmirpur__reb/', views.Shahmirpur__REB, name='shahmirpur__reb'),
    path('julda__reb/', views.Julda__REB, name='julda__reb'),
    path('madunaaghat__reb/', views.Madunaghat__REB, name='madunaaghat__reb'),
    path('chandroghuna__reb/', views.Chandroghuna__REB, name='chandroghuna__reb'),
    path('duhazari__reb/', views.Duhazari___REB, name='duhazari__reb'),
    path('coxsbazar__reb/', views.CoxBazar__REB, name='coxsbazar__reb'),
    path('matarbari__reb/', views.Matarbari__REB, name='matarbari__reb'),
    path('baroiarhat__reb/', views.Baroiarhat__REB, name='baroiarhat__reb'),
    path('shikalbhaha__reb/', views.Shikalbhaha__REB, name='shikalbhaha__reb'),
    path('tk132__reb/', views.TK__REB, name='tk132__reb'),

]

