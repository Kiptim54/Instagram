# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-11 11:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0006_auto_20180511_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photos',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to='instagram.Profile'),
        ),
    ]
