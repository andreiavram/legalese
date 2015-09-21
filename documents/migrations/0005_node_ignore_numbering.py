# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0004_auto_20150519_2221'),
    ]

    operations = [
        migrations.AddField(
            model_name='node',
            name='ignore_numbering',
            field=models.BooleanField(default=False),
        ),
    ]
