from django.urls import path
from . import views
#pdf
from .pdf import data_pdf 

app_name = "dashboard"

urlpatterns = [
     #pdf
    path('pdf/', data_pdf, name='pdf'),


    
    path('', views.dashboard_page, name='dashboard_page'),
    path('home/', views.Home_page, name='Home_page')
]
