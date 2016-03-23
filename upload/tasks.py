from __future__ import absolute_import
from celery import shared_task
from upload.models import Upload
import subprocess
import time

@shared_task
def runscript(current_id, name, path):
    u = Upload.objects.get(id=current_id)
    u.start_job()    
    try:
	print 'try'
	subprocess.check_call(["/home/seb/project/djangoservice/upload/scripts/submit.sh", name, path, str(current_id)]) #add last 2 opts
    except:
        print "An error has occured with job: " + current_id
        u.job_error()
	raise NameError('submit.sh error')
#TODO error handling for dropped connection etc. test which ones would be raised

    print 'job done id: ' + str(current_id)
    result = '/home/seb/project/djangoservice/media/results/' + str(u.author.id) + '_' + str(current_id) + '/co-prediction.txt' 
    u.save_result(result)
    u.job_done()
    print str(current_id) + ' result saved: ' + u.result.path
