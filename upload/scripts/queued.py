from upload.models import *
import subprocess

def run():
    print 'started'
    q = Queue.objects.get(name='testQ')
    u = Upload.objects.get(title='axx')
    q.add_job(u)
    current = q.jobs_list.get()
   # if(q.empty()!= True):
    print subprocess.check_output(['/home/seb/project/djangoservice/upload/scripts/wait.sh', 'a', 'b'], shell=True)
    print 'done'

