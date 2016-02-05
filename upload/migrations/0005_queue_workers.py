# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0004_auto_20160204_1626'),
    ]

    operations = [
        migrations.AddField(
            model_name='queue',
            name='workers',
            field=models.IntegerField(default=1),
        ),
    ]
