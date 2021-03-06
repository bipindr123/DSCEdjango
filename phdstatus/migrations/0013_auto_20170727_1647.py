# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-27 11:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('phdstatus', '0012_remove_phd_status_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='phd_status',
            name='details',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='t_details', to='phdstatus.T_details'),
        ),
        migrations.AlterField(
            model_name='t_details',
            name='duration',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Duration'),
        ),
        migrations.AlterField(
            model_name='t_details',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Name'),
        ),
    ]
