# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-12 13:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0009_photos_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photos',
            name='user',
        ),
    ]
