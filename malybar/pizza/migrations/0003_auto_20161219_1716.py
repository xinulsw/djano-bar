# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-12-19 16:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0002_pizza_autor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skladnik',
            name='nazwa',
            field=models.CharField(max_length=30, verbose_name='sk\u0142adnik'),
        ),
    ]
