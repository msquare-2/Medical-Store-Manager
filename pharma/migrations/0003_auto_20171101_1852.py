# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-01 13:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('pharma', '0002_auto_20171101_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='phn_no',
            field=models.BigIntegerField(max_length=30),
        ),
        migrations.AlterField(
            model_name='order',
            name='qty',
            field=models.IntegerField(max_length=30),
        ),
    ]
