# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-03-26 16:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('races', '0004_race'),
    ]

    operations = [
        migrations.AddField(
            model_name='race',
            name='workers',
            field=models.ManyToManyField(related_name='races', to='races.User'),
        ),
    ]
