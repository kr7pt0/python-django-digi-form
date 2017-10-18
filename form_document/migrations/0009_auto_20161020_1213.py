# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-10-20 01:13
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form_document', '0008_auto_20161020_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fixedformdocument',
            name='document_mapping',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='fixedformdocument',
            name='form_data',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=dict, null=True),
        ),
    ]