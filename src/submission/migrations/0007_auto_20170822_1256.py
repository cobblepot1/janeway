# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-22 12:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('submission', '0006_field_journal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fieldanswer',
            name='field',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='submission.Field'),
        ),
    ]