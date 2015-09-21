# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0005_node_ignore_numbering'),
    ]

    operations = [
        migrations.AddField(
            model_name='node',
            name='is_alternate',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='node',
            name='numbering_type',
            field=models.CharField(default=b'none', max_length=255, choices=[(b'numbers', 'Numbers'), (b'roman', 'Roman numbers'), (b'letters', 'Letters'), (b'dashes', 'Dashes'), (b'none', 'No numbering')]),
        ),
        migrations.AlterField(
            model_name='node',
            name='overall_numbering_type',
            field=models.CharField(default=b'none', max_length=255, null=True, blank=True, choices=[(b'numbers', 'Numbers'), (b'roman', 'Roman numbers'), (b'letters', 'Letters'), (b'dashes', 'Dashes'), (b'none', 'No numbering')]),
        ),
    ]
