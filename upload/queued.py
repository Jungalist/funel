import django
from django.conf import settings

if not settings.configured:
    settings.configure(DEBUG=True)
django.setup()


from upload.models import Queue

print 'hi'
#q = Queue.objects.get(name='testQ')
#current = q.jobs_list.get()
#if(q.empty()!= True):
 #   subprocess.check_output(['/home/seb/project/djangoservice/upload/scripts/wait.sh', current.title, current.file.path], shell=True)


