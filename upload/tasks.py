from __future__ import absolute_import
from celery import shared_task
from upload.models import Upload
import subprocess
import time

@shared_task
def runscript(current_id, name, path):
    u = Upload.objects.get(id=current_id)
    u.start_job()    
    subprocess.check_call(["/home/seb/project/djangoservice/upload/scripts/submit.sh", name, path]) #add last 2 opts
    u.job_done()
    print 'job done id: ' + str(current_id)    
