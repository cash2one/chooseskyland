# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-09-06 02:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20160906_0032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activities',
            name='upLoadImg1',
            field=models.FileField(blank=True, null=True, upload_to='img/', verbose_name='活动封面'),
        ),
        migrations.AlterField(
            model_name='news',
            name='upLoadImg1',
            field=models.FileField(blank=True, null=True, upload_to='img/', verbose_name='活动封面'),
        ),
    ]
