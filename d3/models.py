from django.db import models

class Graph(models.Model):
    assoc_job = models.OneToOneField(
    	'upload.Upload', 
    	on_delete=models.CASCADE,
        primary_key=True,
        default="0000",
        related_name='associd')

   # assoc_job = models.ForeignKey(related_name=id) 
    json_data = models.FileField(null=True)

    graph = models.TextField(null=True)

    #Methods here to generate json and graph
