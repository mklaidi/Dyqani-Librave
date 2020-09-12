from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from .forms import UserLoginForm, UserSignupForm
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth import login,logout

# Create your views here.
def loginview(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            try:
                usr = User.objects.get(username=username)
            except User.DoesNotExist:
                try:
                    usr = User.objects.get(email=username)
                except User.DoesNotExist:
                    form.add_error("username", "Username or email does not exist")
                else:
                    if not check_password(password, usr.password):
                        form.add_error("password", "Wrong password")
                    else:
                        login(request,usr,backend="django.contrib.auth.backends.ModelBackend")
                        return HttpResponseRedirect('/')
            else:
                if not check_password(password, usr.password):
                    form.add_error("password", "Wrong password")
                else:
                    login(request,usr,backend="django.contrib.auth.backends.ModelBackend")
                    return HttpResponseRedirect('/')
    else:
        form = UserLoginForm()
    context = {
        'form': form
    }
    return render(request, "login/login.html", context)

def signupview(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            usr = User(username=username,email=email,password=password)
            usr.save()
            login(request,usr,backend="django.contrib.auth.backends.ModelBackend")
            return HttpResponseRedirect('/')
    else:
        form = UserSignupForm()
    context = {
        'form': form
    }
    return render(request, "login/signup.html", context)

def logoutview(request):
    logout(request)
    return HttpResponseRedirect('/')