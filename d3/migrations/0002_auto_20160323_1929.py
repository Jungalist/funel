# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0014_upload_error'),
        ('d3', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='graph',
            name='id',
        ),
        migrations.RemoveField(
            model_name='graph',
            name='num_attributes',
        ),
        migrations.AddField(
            model_name='graph',
            name='assoc_job',
            field=models.OneToOneField(related_name='assoc_id', primary_key=True, default=b'0000', serialize=False, to='upload.Upload'),
        ),
        migrations.AddField(
            model_name='graph',
            name='file',
            field=models.OneToOneField(related_name='fi_le', default=b'', to='upload.Upload'),
        ),
        migrations.AddField(
            model_name='graph',
            name='graph',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='graph',
            name='json',
            field=models.FileField(null=True, upload_to=b''),
        ),
    ]
