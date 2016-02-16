# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0005_queue_workers'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Queue',
        ),
        migrations.AddField(
            model_name='upload',
            name='finish_date',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
