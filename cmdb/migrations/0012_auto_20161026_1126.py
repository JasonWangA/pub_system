# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-26 03:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0011_auto_20161026_1104'),
    ]

    operations = [
        migrations.AddField(
            model_name='logger',
            name='app',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cmdb.App'),
        ),
        migrations.AlterField(
            model_name='logger',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]