# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-12 12:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Publications', '0011_auto_20170712_1815'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='page_no',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='publication',
            name='volume',
            field=models.IntegerField(blank=True, default=1),
            preserve_default=False,
        ),
    ]
