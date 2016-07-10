from __future__ import absolute_import
from celery import shared_task
from .models import Upload
from newuser.models import EmailUser
import subprocess
import time
from django.core.mail import send_mail
from django.core.urlresolvers import reverse

@shared_task
def runscript(current_id, author_id, name, path, setting, permutations, biohel_runs, attributes):
    u = Upload.objects.get(id=current_id)
    user = EmailUser.objects.get(id=author_id)
    u.author = user
    u.save()
    u.start_job()
    try:
        subprocess.check_call(["/home/seb/project/funel/upload/static/scripts/submit.sh", str(name), str(path), str(current_id), str(setting), str(permutations), str(biohel_runs), str(attributes)])
    except:
        print "An error has occured with job: " + str(current_id)
        #print "Values: " + str(current_id) + str(name) + str(path) + str(setting) + str(permutations) + str(biohel_runs) + str(attributes)
        u.job_error()
        raise NameError('submit.sh error - check HPC logs and make sure connection has not dropped')
#TODO error handling for dropped connection etc. test which ones would be raised

    print 'job done id: ' + str(current_id)
    result = '/home/seb/project/funel/media/results/' + str(u.author.id) + '_' + str(current_id) + '/co-prediction.txt' 
    u.save_result(result)
    print 'before jobdone author: ' + str(u.author.id)
    u.job_done()
    user = EmailUser.objects.get(id=u.author.id)

    token = user.token
#TODO chnage hardcoded url
    send_mail('Your Funel Network Has Been Generated', 
    'Your Funel Network Has Been Generated. Please follow this link to see the results:\n http://127.0.0.1:8000/login/email/%s' % str(token), #+ reverse('email_login', kwargs={'token':token}), 
        's.smolorz@ncl.ac.uk', [str(user.email)], fail_silently=False)
    print str(current_id) + ' result saved: ' + u.result.path


