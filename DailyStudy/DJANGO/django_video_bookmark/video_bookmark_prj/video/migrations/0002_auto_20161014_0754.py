# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-14 07:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='address',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='video',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='videocategory',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
