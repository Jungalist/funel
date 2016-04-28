from __future__ import absolute_import
from celery import shared_task
from .models import Upload
import subprocess
import time


@shared_task
def runscript(current_id, name, path, setting, permutations, biohel_runs, attributes):
    u = Upload.objects.get(id=current_id)
    u.start_job()
    try:
        subprocess.check_call(["/home/seb/project/funel/upload/scripts/submit.sh", str(name), str(path), str(current_id), str(setting), str(permutations), str(biohel_runs), str(attributes)])
    except:
        print "An error has occured with job: " + str(current_id)
        #print "Values: " + str(current_id) + str(name) + str(path) + str(setting) + str(permutations) + str(biohel_runs) + str(attributes)
        u.job_error()
        raise NameError('submit.sh error')
#TODO error handling for dropped connection etc. test which ones would be raised

    print 'job done id: ' + str(current_id)
    result = '/home/seb/project/funel/media/results/' + str(u.author.id) + '_' + str(current_id) + '/co-prediction.txt' 
    u.save_result(result)
    u.job_done()
    print str(current_id) + ' result saved: ' + u.result.path


