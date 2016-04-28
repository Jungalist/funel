from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.core.signals import request_finished
from .models import EmailUser
from django.shortcuts import redirect


def login(request):
#TODO and is valid
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return render(request, 'upload/index.html', {'msg': 'Welcome back'})
            else:
                return render(request, 'upload/index.html', {'msg': 'Account disabled'})
        else:
            return render(request, 'registration/login.html', {'msg': 'Try logging in again'})
    else:
        return render(request, 'registration/login.html', {})

def profile(request):
    user = request.user
    html = "<html><body>Welcome %s.</body></html>" % user
    return HttpResponse(html)
#check if password is set first



#from django.contrib.auth import login
#if logged in, log out or check cookie and login if same user maybe prompt with last seen date
def email_login(request, token):
    user = EmailUser.objects.get(token=token)
    user.backend = 'django.contrib.auth.backends.ModelBackend'
    auth_login(request, user)
    return redirect('/user/show_jobs/')