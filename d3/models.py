from django.db import models
from upload.models import Upload

class Graph(models.Model):
    assoc_job = models.OneToOneField(
    	Upload, 
    	on_delete=models.CASCADE,
        primary_key=True,
        default="0000",
        related_name='associd')

    json_data = models.FileField(null=True)

    graph = models.TextField(null=True)

    #Methods here to generate json and graph
