from __future__ import absolute_import
from celery import shared_task
import subprocess
import time

@shared_task
def runscript(id, path):
    #ssh in
    #pass to script
    #wait script
    #send back results
    #close connection
    #time.sleep(2)
    #tmp = "/home/seb/project/djangoservice/media/results/" + str(id) +".txt"
    #text_file = open(tmp , "w+")
    #text_file.write("Waited 5")
    #text_file.write("Job number: " + str(id))
    #text_file.close()
    subprocess.call(["/home/seb/project/djangoservice/upload/scripts/submit.sh", path])
