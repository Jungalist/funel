from django.db import models
from django.utils import timezone
import Queue
import threading
import subprocess

class Upload(models.Model):
#    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=20)
    status = models.BooleanField(default=False)
    submit_date = models.DateTimeField(
            default=timezone.now)
    start_date = models.DateTimeField(
            blank=True, null=True)
    file = models.FileField(upload_to='uploads', null=True)

    def start_job(self):
        self.start_date = timezone.now()
        self.save()

    def get_status(self):
        return self.status

    def __str__(self):
        return self.title

class Queue(models.Model):
    max_size = models.IntegerField(default=20)
    name = models.CharField(max_length=20)
    jobs_list = Queue.Queue()
    workers = models.IntegerField(default=1)

    def __str__(self):
        return self.name

    def add_job(self, job):
        self.jobs_list.put(job)
	self.save()
	return

    def empty(self):
        return self.jobs_list.empty()

    #start the job, pop from queue, wait til it finishes 
    def get(self):
	current = self.jobs_list.get()
	subprocess.check_output(['/home/seb/project/djangoservice/upload/scripts/wait.sh', current.title, current.file.path], shell=True)
	return
    
    #def all_jobs(self):
#	job_names = {}
#	while(!self.jobs_list.empty()):
	    #addend to dictionary with name as key and object as value?
#	    job_names[self.get().name] = 
