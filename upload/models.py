from django.db import models
from django.utils import timezone
import threading
import subprocess
import uuid
from django.conf import settings
from d3.scripts.convert import convert
from d3.models import Graph

class Upload(models.Model):
    SETTINGS = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
    )

    PERMUTATIONS = (
        ('10', '10'),
        ('50', '50'),
        ('100', '100'),
        ('200', '200'),
    )

    BIOHEL = (
        ('250', '250'),
        ('500', '500'),
        ('1000', '1000'),
        ('2500', '2500'),
    )

    ATTRIBUTES = (
        ('10', '10'),
        ('50', '50'),
        ('100', '100'),
        ('200', '200'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
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
    setting = models.PositiveSmallIntegerField(default=1, choices=SETTINGS)
    permutations = models.PositiveSmallIntegerField(default=100, choices=PERMUTATIONS)
    biohel_runs = models.PositiveSmallIntegerField(default=1000, choices=BIOHEL)
    attributes = models.PositiveSmallIntegerField(default=100, choices=ATTRIBUTES)

    def start_job(self):
        self.start_date = timezone.now()
        self.save()

    def get_status(self):
        return self.status

    #Once the job is finished, generate the JSON file and create a corresponding Graph object
    #TODO change id permamently
    def job_done(self):
        self.finish_date = timezone.now()
        json_file = convert(self.result.path, str(self.author.id) + str(self.id))
        Graph.objects.create(assoc_job_id=self.id, json_data=json_file)
        self.status = True
        self.save()

    def __str__(self):
        return str(self.id)

    def save_result(self, r):
        self.result = r

        self.save()

#TODO use this
    def job_error(self):
        self.status = False
        self.error = True
        self.save()

    def job_fixed(self):
        self.error = False
        self.save()