from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .forms import Saveinfo
from django.contrib.auth.models import User


# Create your views here.


def signupview(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        global user
        user=request.POST.get('username')
        if form.is_valid():
            user=form.save()
            login(request, user)
            return redirect('accounts:saveinfo')
    else:
        form=UserCreationForm()
    return render(request, 'loginapp/signup.html', {'form':form})


def loginview(request):
    if request.method=="POST":
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('articles:home')
    else:
        form=AuthenticationForm()
    return render(request, 'loginapp/login.html', {'form':form})


def logoutview(request):
    if request.method=="POST":
        logout(request)
        return redirect('articles:home')


def saveinfoview(request):
    global user
    if request.method=="POST":
        a=User.objects.get(username=user)
        form=Saveinfo(request.POST, request.FILES, instance=a)
        email=request.POST.get('email')
        emails=User.objects.filter(email=email)
        if len(emails)==1:
            return redirect('/accounts/signup/saveinfo/?novalid1')
        else:
            if form.is_valid():
                form.save()
                return redirect('articles:home')
            else:
                return redirect('/accounts/signup/saveinfo/?novalid2')
    else:
        form=Saveinfo()
    return render(request, 'loginapp/saveinfo.html', {'form':form})

