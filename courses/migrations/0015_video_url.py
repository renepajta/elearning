# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-20 11:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0014_auto_20170720_1317'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='url',
            field=models.URLField(default=''),
        ),
    ]
