from django.db import models
from django.utils import timezone
import threading
import subprocess
from django.contrib.auth.models import User

class Upload(models.Model):
    author = models.OneToOneField(User, default=None)#, default=str('herro'))#on_delete=models.CASCADE) #TODO change
    title = models.CharField(max_length=20)
    status = models.BooleanField(default=False)
    submit_date = models.DateTimeField(
            default=timezone.now)
    start_date = models.DateTimeField(
            blank=True, null=True)
    finish_date = models.DateTimeField(
            blank=True, null=True)
    file = models.FileField(upload_to='uploads', null=True)

    def start_job(self):
        self.start_date = timezone.now()
        self.save()

    def get_status(self):
        return self.status

    def job_done(self):
	self.finish_date = timezone.now()
	self.save()

    def __str__(self):
        return self.title

