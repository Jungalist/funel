from django.shortcuts import render
from django.shortcuts import redirect
from .forms import UploadFileForm
from .models import Upload
from newuser.models import EmailUser
from upload.tasks import runscript
import os
from django.conf import settings
from django.contrib.auth import logout
from django.contrib import auth
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.views.static import serve
#import pdb; pdb.set_trace() -debug

def upload_view(request):  
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        #TODO check all fields that need to be saved are
    #add an in.progress var
    #use PK ids to refer to uplaods
        if form.is_valid():
            email = request.POST['email']
            user = EmailUser.objects.filter(email=email)
            if not user:
                logout(request)
                user = EmailUser.objects.create(email=email)
                user.backend = 'django.contrib.auth.backends.ModelBackend'
                auth_login(request, user)
            else: 
                user = EmailUser.objects.get(email=email)
            print user.id
            upload = form.save()
            upload.title = request.POST['title']
            upload.author.id = user.id#may be redundant
            upload.save()
            path = change_name(upload)
            runscript.delay(upload.id, str(user.id), (str(upload.author.id) + '_' + str(upload.id)), path, upload.setting, upload.permutations, upload.biohel_runs, upload.attributes)
            return render(request, 'upload/submitted.html', {'title': upload.title, 'link': 'job/' + str(upload.id)})

    else:
        user = request.user
        if user.id is not None:
            form = UploadFileForm(initial={'email': user})
        else:
            form = UploadFileForm(initial={'email': ''})

        
        #do some logic to handle new user

    
    return render(request, 'upload/upload_view.html', {'form': form})


def index(request):
    return render(request, 'upload/index.html', {'user': request.user})

#TODO file extension 
#TODO split into files/classes
def change_name(u):
    old = u.file.path
    new = settings.MEDIA_ROOT + '/' + 'experiments' + '/' + str(u.author.id) + '_' + str(u.id) + '.arff'
    os.rename(old, new)
    setattr(u, 'file', new)
    u.save()
    return new

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

def result(request, id):
    #TODO dont hardcode getting the object and paths where possible
    u = Upload.objects.get(id=id)

    if (request.user != u.author):
         return render(request, 'upload/log.html')
    else:
        return render(request, 'upload/result.html', {'id': id})


def download(request, id):
    u = Upload.objects.get(id=id)
    print u.result
    response = HttpResponse(u.result, content_type='application/text/plain')
    response['Content-Disposition'] = 'attachment; filename="results.txt"'
    return response


