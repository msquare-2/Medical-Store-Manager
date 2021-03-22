# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-07 13:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('pharma', '0006_remove_order_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dealer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('d_id', models.IntegerField()),
                ('fname', models.CharField(max_length=30)),
                ('lname', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=100)),
                ('phn_no', models.BigIntegerField()),
                ('email', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='member',
            name='phn_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pharma.Dealer'),
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]
