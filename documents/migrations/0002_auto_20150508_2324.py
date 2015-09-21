# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='node',
            name='overall_numbering_format',
            field=models.CharField(default=b'%%s', max_length=255),
        ),
        migrations.AddField(
            model_name='node',
            name='overall_numbering_type',
            field=models.CharField(default=b'none', max_length=255, choices=[(b'numbers', 'Numbers'), (b'roman', 'Roman numbers'), (b'letters', 'Letters'), (b'none', 'No numbering')]),
        ),
        migrations.AddField(
            model_name='node',
            name='overall_order',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
