from django.urls import path
from . import views

app_name="gridload"

urlpatterns = [
    
    path('show/', views.Grid_load_show, name='Grid_load_show'),
    path('user/', views.Grid_load_input, name='Grid_load_input'),
    path('pdb-reb/', views.PDB_RRB, name='PDB_RRB'),
    path('pdb-reb-shed/', views.PDB_RRB_shed, name='PDB_RRB_shed'),
    path('reb-load/', views.REB_load, name='REB_load'),


   
    
]
