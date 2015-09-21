# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0009_auto_20150919_0029'),
    ]

    operations = [
        migrations.AddField(
            model_name='node',
            name='depth',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='node',
            name='numbering_format',
            field=models.CharField(default=b'%%i', max_length=255),
        ),
    ]
