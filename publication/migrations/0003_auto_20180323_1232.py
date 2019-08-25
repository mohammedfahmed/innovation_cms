# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-23 12:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('publication', '0002_auto_20180214_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='_type',
            field=models.ForeignKey(error_messages={'blank': 'Publication Type can not be empty.'}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='events', to='publication.PublicationType'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='address',
            field=models.CharField(error_messages={'blank': 'Address can not be empty.', 'max_length': 'Address must be less than 255 characters.'}, max_length=255, null=True, verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='book_title',
            field=models.CharField(error_messages={'blank': 'Book Title can not be empty.', 'max_length': 'Book Title must be less than 100 characters.'}, max_length=100, null=True, verbose_name='Book Title'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='end_page',
            field=models.IntegerField(error_messages={'blank': 'End Page can not be empty.'}, null=True, verbose_name='End Page'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='institution',
            field=models.CharField(error_messages={'blank': 'Institution can not be empty.', 'max_length': 'Institution must be less than 100 characters.'}, max_length=100, null=True, verbose_name='Institution'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='note',
            field=models.TextField(error_messages={'blank': 'Note can not be empty.'}, null=True, verbose_name='Note'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='number',
            field=models.IntegerField(error_messages={'blank': 'Publication Number can not be empty.'}, null=True, verbose_name='Publication Number'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='publisher',
            field=models.CharField(error_messages={'blank': 'Publisher can not be empty.', 'max_length': 'Publisher must be less than 100 characters.'}, max_length=100, null=True, verbose_name='Publisher'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='start_page',
            field=models.IntegerField(error_messages={'blank': 'Start Page can not be empty.'}, null=True, verbose_name='Start Page'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='volume',
            field=models.IntegerField(error_messages={'blank': 'Publication Volume can not be empty.'}, null=True, verbose_name='Publication Volume'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='year',
            field=models.IntegerField(error_messages={'blank': 'Publication Year can not be empty.'}, null=True, verbose_name='Publication Year'),
        ),
    ]