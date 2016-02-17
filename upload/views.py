from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import UploadFileForm
from .models import Upload
from upload.tasks import runscript
from django.contrib.auth.models import User
import subprocess


#import pdb; pdb.set_trace() -debug



def upload_view(request):  
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        #TODO check all fields that need to be saved are
	#add an in.progress var
	#use PK ids to refer to uplaods
        if form.is_valid():
	    title = form.instance.title	    
	    runscript.delay(title)
	    form.save()
	    #refresh() #TODO add concurrency number variable for admin
	    return render(request, 'upload/submitted.html', {'title': title})
    else:
        form = UploadFileForm()
    
    return render(request, 'upload/upload_view.html', {'form': form})


def index(request):
    user = request.user
    return render(request, 'upload/index.html', {'user': user})


#def login(request):
#    

#def logout(request):
#    return

def getName(path):
    s = ""
    for c in reversed(path):
        while c != '/':
            s = s + c
    return reversed(s)

    
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return render(request, 'upload/index.html', {'msg': 'Welcome back'})
        else:
            return render(request, 'upload/index.html', {'msg': 'Account disabled'})
    else:
        return render(request, 'upload/login.html', {'msg': 'Try logging in again'})

