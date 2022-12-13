from django.urls import path
from . import views

app_name = 'GEN'

urlpatterns = [
    path('genall/', views.Generation_Disply, name='Generation_Disply'),
    path('gen11/', views.Generation_11AM, name='Generation_11AM'),
    path('gen19/', views.Generation_19PM, name='Generation_19PM'),
    path('genhr/', views.Generation_33kv, name='Generation_33kv'),
    path('gen/', views.Generation_page_link, name='Generation_page_link'),
]
