from django.db import models
from upload.models import Upload

class Graph(models.Model):
    #assoc_job = models.ForeignKey('Upload.id')
    num_attributes = models.IntegerField(default=0)
    #file = models.ForeignKey('Upload.file')

