from __future__ import absolute_import
from celery import shared_task

import subprocess


@shared_task
def add(x, y):
    return x + y

@shared_task
def runscript(p):
    subprocess.check_call(['/home/seb/project/djangoservice/upload/scripts/wait.sh', p])
    return
