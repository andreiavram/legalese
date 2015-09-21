# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0006_auto_20150918_2335'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='node',
            name='is_alternate',
        ),
        migrations.AddField(
            model_name='node',
            name='alternate_marker',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
    ]
