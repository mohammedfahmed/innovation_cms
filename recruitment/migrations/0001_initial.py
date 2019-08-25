# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-10 18:27
from __future__ import unicode_literals

import audit_log.models.fields
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Recruitment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_with_session_key', audit_log.models.fields.CreatingSessionKeyField(editable=False, max_length=40, null=True)),
                ('modified_with_session_key', audit_log.models.fields.LastSessionKeyField(editable=False, max_length=40, null=True)),
                ('creation_datetime', models.DateTimeField(auto_now_add=True)),
                ('last_modified_datetime', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(db_index=True, default=False, editable=False)),
                ('position', models.CharField(error_messages={'blank': 'Position can not be empty.', 'max_length': 'Position must be less than 255 characters.', 'null': 'Position is a required field.'}, max_length=255, verbose_name='Position')),
                ('program', models.CharField(error_messages={'blank': 'Company can not be empty.', 'max_length': 'Company must be less than 255 characters.', 'null': 'Company is a required field.'}, max_length=255, verbose_name='Company')),
                ('start_datetime', models.DateTimeField(default=datetime.datetime.now)),
                ('job_description', models.TextField(error_messages={'blank': 'Job Description can not be empty.', 'null': 'Job Description is a required field.'}, verbose_name='Job Description')),
                ('created_by', audit_log.models.fields.CreatingUserField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_recruitment_recruitment_set', to=settings.AUTH_USER_MODEL, verbose_name='created by')),
                ('modified_by', audit_log.models.fields.LastUserField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='modified_recruitment_recruitment_set', to=settings.AUTH_USER_MODEL, verbose_name='modified by')),
            ],
            options={
                'verbose_name_plural': 'Recruitments',
                'verbose_name': 'Recruitment',
            },
        ),
    ]
