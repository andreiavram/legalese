# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0008_document_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='root_numbering',
            field=models.CharField(default=b'none', max_length=255),
        ),
        migrations.AddField(
            model_name='document',
            name='root_numbering_format',
            field=models.CharField(default=b'%%i', max_length=255),
        ),
        migrations.AlterField(
            model_name='node',
            name='overall_numbering_format',
            field=models.CharField(default=b'%%i', max_length=255, null=True, blank=True),
        ),
    ]
