# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-23 22:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('d3', '0002_auto_20160323_1929'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='graph',
            name='file',
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