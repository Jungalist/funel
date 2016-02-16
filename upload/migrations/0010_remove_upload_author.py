# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0009_auto_20160216_1212'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='upload',
            name='author',
        ),
    ]
