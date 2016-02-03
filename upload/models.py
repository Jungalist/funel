from django.db import models
from django.utils import timezone

class Upload(models.Model):
#    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=20)
    status = models.BooleanField(default=False)
    submit_date = models.DateTimeField(
            default=timezone.now)
    start_date = models.DateTimeField(
            blank=True, null=True)
    file = models.FileField(upload_to='media', null=True)

    def start_job(self):
        self.start_date = timezone.now()
        self.save()

    def get_status(self):
        return self.status

    def __str__(self):
        return self.title
