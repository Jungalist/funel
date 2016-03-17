# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0013_upload_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='upload',
            name='error',
            field=models.BooleanField(default=False),
        ),
    ]
