# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-28 00:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newuser', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailuser',
            name='token',
            field=models.UUIDField(blank=True, null=True),
        ),
    ]