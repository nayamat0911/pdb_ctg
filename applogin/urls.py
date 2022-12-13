from django.urls import path
from . import views
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView,PasswordResetCompleteView

app_name = "applogin"


urlpatterns = [
    
    path('', views.user_login, name='userlogin'),
    path('signup/', views.User_signup, name='usersignup'),
    path('logout/', views.User_logout, name='userlogout'),
    path('profile/', views.Profile, name='profile'),

    # change password
    path('change_pass/', views.Change_pass, name='Change_pass'),
    path('change_pass1/', views.Change_pass_without_old, name='Change_pass_without_old'),

    # reset password
    path('reset/password/', PasswordResetView.as_view(template_name='session/reset_passowr.html'), name='password_reset'),
    path('reset/password/done/', PasswordResetDoneView.as_view(template_name='session/reset_password_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='session/reset_password_confrim.html'), name='password_reset_confirm'),
    path('reset/done/', PasswordResetView.as_view(template_name='session/password_reset_complete.html'), name='password_reset_complete'),


]
