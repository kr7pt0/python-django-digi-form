# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-18 10:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import form_document.models


class Migration(migrations.Migration):

    dependencies = [
        ('form_document', '0004_auto_20160616_1848'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormDocumentAssets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=form_document.models.document_path)),
            ],
        ),
        migrations.RemoveField(
            model_name='formdocument',
            name='processed_documents',
        ),
        migrations.AddField(
            model_name='formdocumentassets',
            name='form_document',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form_document.FormDocument'),
        ),
    ]