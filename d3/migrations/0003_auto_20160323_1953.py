# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('d3', '0002_auto_20160323_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='graph',
            name='assoc_job',
            field=models.OneToOneField(related_name='associd', primary_key=True, default=b'0000', serialize=False, to='upload.Upload'),
        ),
        migrations.AlterField(
            model_name='graph',
            name='file',
            field=models.OneToOneField(related_name='fiile', default=b'', to='upload.Upload'),
        ),
    ]
