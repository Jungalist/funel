from django.shortcuts import render
from django.shortcuts import redirect
from .forms import UploadFileForm
from .models import Upload
from django.contrib import auth
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from upload.tasks import runscript
import os
from django.conf import settings
#import pdb; pdb.set_trace() -debug

def upload_view(request):  
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        #TODO check all fields that need to be saved are
    #add an in.progress var
    #use PK ids to refer to uplaods
        if form.is_valid():
        upload = form.save()
        path = change_name(upload)
        runscript.delay(upload.pk, (str(upload.author.id) + '_' + str(upload.id)), path, setting, permutations, biohel_runs, attributes)
        return render(request, 'upload/submitted.html', {'title': upload.title, 'link': 'job/' + str(upload.id)})
    else:
        form = UploadFileForm()
    
    return render(request, 'upload/upload_view.html', {'form': form})


def index(request):
    return render(request, 'upload/index.html', {'user': request.user})

#TODO file extension 
#TODO split into files/classes
def change_name(u):
    old = u.file.path
    print "old: " + str(old)
    new = settings.MEDIA_ROOT + '/' + 'experiments' + '/' + str(u.author.id) + '_' + str(u.id) + '.arff'
    os.rename(old, new)
    setattr(u, 'file', new)
    u.save()
    print "new: " + new
    return new
    
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

def progress(request, id):
    #TODO only show users their own jobs/do all the view handling logic here not in html
    #TODO check if job isnt already finished
    job = Upload.objects.get(id=id)
    #If the job has been started, change message to 'in progress'
    if (job.start_date is not None):
        if (job.status):
        return redirect('results', id=id)
    else:
        progress = 'We are working on you experiment, check back later'
    else:
    progress = 'Your job is in the queue, please check back later'

    return render(request, 'upload/progress.html', {'progress': progress})

def show_jobs(request):
    jobs = Upload.objects.filter(author=request.user)
    return render(request, 'upload/jobs.html', {'jobs': jobs})

def result(request, id):

    #TODO dont hardcode getting the object and paths where possible
    return render(request, 'upload/result.html', {'id': id})
