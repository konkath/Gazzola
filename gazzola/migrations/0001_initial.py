# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-05 21:09
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=64)),
                ('postal_code', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(99999)])),
                ('street', models.CharField(max_length=64, null=True)),
                ('house_number', models.CharField(max_length=4)),
                ('apt_number', models.CharField(max_length=4, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
                ('surname', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=254)),
                ('reg_date', models.DateField()),
                ('order_count', models.PositiveIntegerField()),
                ('address', models.ManyToManyField(to='gazzola.Address')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('additional_info', models.CharField(max_length=128)),
                ('order_date', models.DateField()),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gazzola.Address')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gazzola.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='OrderedPizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(4)])),
            ],
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pizza_name', models.CharField(max_length=32, unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Pizzeria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gazzola.Address')),
            ],
        ),
        migrations.CreateModel(
            name='Promo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount', models.DecimalField(decimal_places=2, max_digits=5)),
                ('valid_from', models.DateField()),
                ('valid_to', models.DateField()),
                ('pizza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gazzola.Pizza')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('review', models.CharField(max_length=255)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gazzola.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Storeroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(999)])),
            ],
        ),
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.AddField(
            model_name='storeroom',
            name='toppings',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gazzola.Topping'),
        ),
        migrations.AddField(
            model_name='pizzeria',
            name='storeroom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gazzola.Storeroom'),
        ),
        migrations.AddField(
            model_name='pizza',
            name='toppings',
            field=models.ManyToManyField(to='gazzola.Topping'),
        ),
        migrations.AddField(
            model_name='orderedpizza',
            name='pizza',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gazzola.Pizza'),
        ),
        migrations.AddField(
            model_name='order',
            name='pizza',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gazzola.OrderedPizza'),
        ),
    ]
