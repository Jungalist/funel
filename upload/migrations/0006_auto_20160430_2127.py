# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-30 20:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0005_auto_20160427_2309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='upload',
            name='permutations',
            field=models.PositiveSmallIntegerField(choices=[(1, b'1'), (15, b'15'), (50, b'50'), (100, b'100'), (200, b'200')], default=10),
        ),
        migrations.AlterField(
            model_name='upload',
            name='title',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
