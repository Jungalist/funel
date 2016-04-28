from django.shortcuts import render
from django.shortcuts import redirect
from .forms import UploadFileForm
from .models import Upload
from newuser.models import EmailUser
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
            email = request.POST['email']
            user = EmailUser.objects.get(email=email)
            upload = form.save()
            upload.author.id = user.id
            #upload.author = user
            #it gets set correctly here but as soon as it goes to the task, it shows id as 1 again?!
            print 'form valid view 1: ' + str(upload.author.id)
            upload.save()
            path = change_name(upload)
            print 'user submitted a job: ' + str(upload.author.id)
            runscript.delay(upload.id, str(user.id), (str(upload.author.id) + '_' + str(upload.id)), path, upload.setting, upload.permutations, upload.biohel_runs, upload.attributes)
            print 'form valid view 2: ' + str(upload.author.id)
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
    print 'views.change_name top: ' + str(u.author.id)
    old = u.file.path
    new = settings.MEDIA_ROOT + '/' + 'experiments' + '/' + str(u.author.id) + '_' + str(u.id) + '.arff'
    os.rename(old, new)
    setattr(u, 'file', new)
    u.save()
    print 'views.change_name bottom: ' + str(u.author.id)
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

def show_jobs(request):
    jobs = Upload.objects.filter(author=request.user)
    message = ''
    if not jobs:
        message = 'You have no jobs'
    return render(request, 'upload/jobs.html', {'jobs': jobs, 'message': message})

def result(request, id):

    #TODO dont hardcode getting the object and paths where possible
    return render(request, 'upload/result.html', {'id': id})
