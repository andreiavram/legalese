# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import documents.models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0011_document_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentProvider',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('logo', models.ImageField(null=True, upload_to=documents.models.document_provider_upload_to, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='document',
            name='provider',
            field=models.ForeignKey(default=1, to='documents.DocumentProvider'),
            preserve_default=False,
        ),
    ]
