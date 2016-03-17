from django.db import models
from django.utils import timezone
import threading
import subprocess
from django.conf import settings

class Upload(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    title = models.CharField(max_length=20)
#TODO - change status to be a text field and merge with error
    status = models.BooleanField(default=False)
    error = models.BooleanField(default=False)
    submit_date = models.DateTimeField(
            default=timezone.now)
    start_date = models.DateTimeField(
            blank=True, null=True)
    finish_date = models.DateTimeField(
            blank=True, null=True)#TODO change to unique name
    file = models.FileField(upload_to='experiments', null=True)
    result = models.FileField(null=True)

    def start_job(self):
        self.start_date = timezone.now()
        self.save()

    def get_status(self):
        return self.status

    def job_done(self):
	self.finish_date = timezone.now()
        self.status = True
	self.save()

    def __str__(self):
        return self.title

    def save_result(self, r):
        self.result = r
        self.save()

    def job_error(self):
	self.status = False
	self.error = True
	self.save()

    def job_fixed(self):
	self.error = False
	self.save()
