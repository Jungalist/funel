from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import UploadFileForm
from .models import Upload
from .models import Queue
import subprocess

def upload_view(request):  
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
	q = Queue.objects.get(name='testQ')
        #TODO check all fields that need to be saved are
	#add an in.progress var
	#use PK ids to refer to uplaods
        if form.is_valid():
	    title = form.instance.title
	    q.add_job(title)
	    form.save()
	    #path = instance.file.path
            #subprocess.call(['/home/seb/project/djangoservice/upload/scripts/wait.sh'], shell=True)
	    #refresh() #TODO add time variable that can be set in admin
            #return HttpResponseRedirect('success/') # IMPLEMENT
	    return render(request, 'upload/submitted.html', {'title': title})
    else:
        form = UploadFileForm()
    
    return render(request, 'upload/upload_view.html', {'form': form})

def success(request):
    return render(request, 'upload/submitted.html',{})

#Where the fuck do I put this?
def start_job(q):
    current = q.jobs_list.get()
    subprocess.check_output(['/home/seb/project/djangoservice/upload/scripts/wait.sh', current.title, current.file.path], shell=True)



def getName(path):
    s = ""
    for c in reversed(path):
        while c != '/':
            s = s + c
    return reversed(s)    
