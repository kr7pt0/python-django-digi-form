# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-09-20 04:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import form_document.models


class Migration(migrations.Migration):

    dependencies = [
        ('form_document', '0002_formdocumenttemplate_cached_form'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormDocumentResponseAttachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attachment', models.FileField(upload_to=form_document.models.form_document_attachment_path)),
            ],
            options={
                'verbose_name': 'FormDocumentResponseAttachment',
                'verbose_name_plural': 'FormDocumentResponseAttachments',
            },
        ),
        migrations.AddField(
            model_name='formdocumentresponse',
            name='cached_form',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='form_document.FixedFormDocument'),
        ),
        migrations.AddField(
            model_name='formdocumentresponseattachment',
            name='response',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form_document.FormDocumentResponse'),
        ),
    ]
