from django.db import models
from d3.scripts.convertigraph import *
import subprocess



class Graph(models.Model):
    assoc_job = models.OneToOneField(
    	'upload.Upload', 
    	on_delete=models.CASCADE,
        primary_key=True,
        default="0000",
        related_name='associd')

   # assoc_job = models.ForeignKey(related_name=id) 
    json_data = models.FileField(null=True)

    positions = models.FileField(null=True)

    #Methods here to generate json and graph
    def calculate_positions(self, author, result):
        pos = convertigraph(str(result), str(author) + str(self.assoc_job_id))
        subprocess.call(["sudo", "python", "/home/seb/project/funel/d3/scripts/generate.py", pos, str(self.assoc_job_id)])
        self.positions = "/home/seb/project/funel/media/graph/1" + str(self.assoc_job_id) + "/positions.json"