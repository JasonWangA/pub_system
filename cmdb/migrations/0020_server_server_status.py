# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-07 07:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0019_auto_20161101_1007'),
    ]

    operations = [
        migrations.AddField(
            model_name='server',
            name='server_status',
            field=models.BooleanField(default=True),
        ),
    ]