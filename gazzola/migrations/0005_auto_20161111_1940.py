# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-11 18:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gazzola', '0004_auto_20161105_2350'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderedpizza',
            name='pizza',
        ),
        migrations.AddField(
            model_name='orderedpizza',
            name='toppings',
            field=models.ManyToManyField(to='gazzola.Topping'),
        ),
    ]
