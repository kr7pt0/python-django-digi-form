# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-03 00:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_explorer', '0002_auto_20160503_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='afslicenseeentry',
            name='abn',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='afslicenseeentry',
            name='acn',
            field=models.BigIntegerField(null=True),
        ),
    ]
