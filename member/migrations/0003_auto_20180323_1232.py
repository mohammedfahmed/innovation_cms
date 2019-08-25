# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-23 12:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0002_auto_20180214_2014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='full_name',
            field=models.CharField(error_messages={'blank': 'Full Name can not be empty.', 'max_length': 'Full Name must be less than 30 characters.'}, max_length=30, null=True, verbose_name='Full Name'),
        ),
    ]
