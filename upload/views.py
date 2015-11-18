from django.shortcuts import render
from django.http import HttpResponse
from .forms import UploadFileForm
from .models import Upload
import subprocess

def upload_view(request):  
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        #set all the other fields to save form to an upload object in db
	#add an in.progress var
	#use PK ids to refer to uplaods
        if form.is_valid():
            instance = Upload(file=request.FILES['file'])
	    instance.save()
	    path = instance.file.path
            subprocess.call(['/home/seb/project/djangoservice/upload/scripts/wait.sh',(getName(path)+'_test')], shell=True)
	    refresh()#add time variable that can be set in admin
            return HttpRedirect('upload/submitted.html') # IMPLEMENT
    else:
        form = UploadFileForm()
    return render(request, 'upload/upload_view.html', {'form': form})

def refresh():
     subprocess.check_output(["/home/seb/project/djangoservice/upload/scripts/wait.sh", "scripts/hello.txt"], shell=True)

def getName(path):
    s = ""
    for c in reversed(path):
        while c != '/':
            s = s + c
    return reversed(s)    
