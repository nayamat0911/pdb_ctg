from django.shortcuts import render, HttpResponseRedirect, HttpResponse ,redirect
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate, login,logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required

# Create your views here.
# -------------------Login----------*********************************
def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request=request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request, user)
                print('loged in')
                return redirect('dashboard:Home_page')
            else:
                messages.info(request, "Not valid username or password")
                return redirect('applogin:userlogin')
    else:
        form = AuthenticationForm()
    context = {
        'userlogin':form,
    }
    return render(request, 'login/login.html', context=context)


# -------------------Signup section----------*********************************
def User_signup(request):
    
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('applogin:userlogin')
            

    else:    
        form = SignUpForm()
    form = SignUpForm()
    return render(request, 'login/signup.html',{'form':form})



# -------------------Logout section----------*********************************
def User_logout(request):
    logout(request)
    return redirect('applogin:userlogin')

# change password--with old password----------*********************************

# @login_required
def Change_pass(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = PasswordChangeForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                messages.success(request, "Password change Successfully!")
                return redirect('applogin:profile')
        else:
            form = PasswordChangeForm(user=request.user)

        return render(request,'change_pass/change_pass.html', {'form':form})
    else:
        return HttpResponse("You aren't access this page!")


# change password--without old password----------*********************************
def Change_pass_without_old(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = SetPasswordForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                messages.success(request, "Password change Successfully!")
                return redirect('applogin:profile')
        else:
            form = SetPasswordForm(user=request.user)

        return render(request,'change_pass/change_pass.html', {'form':form})
    else:
        return HttpResponse("You aren't access this page!")


# -------------------Profile section----------*********************************
@login_required
def Profile(request):
    return render(request, 'login/profile.html')
    

