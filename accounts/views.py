from django.shortcuts import render,redirect
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.conf import settings

User=settings.AUTH_USER_MODEL

def signup(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == "POST" :
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('posts:index')
    else:
        form=CustomUserCreationForm()
        context={'form':form}
        return render(request,'accounts/signup.html',context)



def login(request) :

    if request.method=="POST" :
        form=AuthenticationForm(request,request.POST)
        if form.is_valid():
            auth_login(request,form.get_user())
        return redirect(request.GET.get('next') or 'posts:index')

    else:
        form = AuthenticationForm()
        context = {'form':form}
        return render(request,'accounts/login.html',context)




def logout(request):
    auth_logout(request)
    return redirect('posts:index')


def delete(request):
    request.user.delete()
    return redirect('posts:index')

