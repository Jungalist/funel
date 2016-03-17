# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0012_auto_20160223_1508'),
    ]

    operations = [
        migrations.AddField(
            model_name='upload',
            name='result',
            field=models.FileField(null=True, upload_to=b''),
        ),
    ]
