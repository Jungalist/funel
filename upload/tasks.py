from celeryapp import Celery
import subprocess

app = Celery('tasks', broker = 'amqp://seb:password@localhost/vhost', backend='amqp')

@app.task
def add(x, y):
    return x + y

@app.task
def runscript():
    subprocess.check_call('/home/seb/project/djangoservice/upload/scripts/wait.sh')
    return
