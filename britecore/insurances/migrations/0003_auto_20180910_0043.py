# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-10 03:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eav', '0002_auto_20161014_0157'),
        ('insurances', '0002_auto_20180909_2123'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='risktypeattribute',
            name='attribute',
        ),
        migrations.RemoveField(
            model_name='risktypeattribute',
            name='risk_type',
        ),
        migrations.AddField(
            model_name='risktype',
            name='attributes',
            field=models.ManyToManyField(to='eav.Attribute'),
        ),
        migrations.DeleteModel(
            name='RiskTypeAttribute',
        ),
    ]
