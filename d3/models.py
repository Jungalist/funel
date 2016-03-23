from django.db import models
from upload.models import Upload

class Graph(models.Model):
    assoc_job = models.OneToOneField(
    	Upload, 
    	on_delete=models.CASCADE,
        primary_key=True,
        default="0000",
        related_name='associd')

    #file = models.OneToOneField(
   # 	Upload, 
    #	default='',
     #   related_name='fiile')

    json = models.FileField(null=True)

    graph = models.TextField(null=True)
