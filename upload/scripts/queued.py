from upload.models import *
import subprocess
import time
import os
import sys

pid = str(os.getpid())
pidfile = "/home/seb/project/djangoservice/tmp/mydaemon.pid"

if os.path.isfile(pidfile):
    print "%s already exists, exiting" % pidfile
    sys.exit()
#print 'before'
file(pidfile, 'w').write(pid)
#print 'after'

try:
    def run():
        print 'started'
        q = Queue.objects.get(name='testQ')
        u = Upload.objects.get(title='axx')
        q.add_job(u)
        current = q.jobs_list.get()
        i = 0
        if(q.empty()):
            while(i<25):
                print 'queue is empty, waiting 5s'
                time.sleep(5)
                print 'check if empty, loop again'
                i += 1
            q.add_job(u)

        else:
            print 'continuing processing'

        print subprocess.call(['/home/seb/project/djangoservice/upload/scripts/wait.sh', 'a', 'b'], shell=True)
        print 'done'

finally:
    os.unlink(pidfile)


#def run():
#    print 'started'
#    q = Queue.objects.get(name='testQ')
#    u = Upload.objects.get(title='axx')
#    q.add_job(u)
#    current = q.jobs_list.get()
#    i = 0
#    if(q.empty()):
#        while(i<25):
#	    print 'queue is empty, waiting 5s'
#	    time.sleep(5)
#	    print 'check if empty, loop again'
#	    i += 1
#	q.add_job(u)
#
#    else:
#	print 'continuing processing'
#
#    print subprocess.call(['/home/seb/project/djangoservice/upload/scripts/wait.sh', 'a', 'b'], shell=True)
#    print 'done'

