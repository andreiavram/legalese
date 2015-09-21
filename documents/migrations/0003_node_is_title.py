# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0002_auto_20150508_2324'),
    ]

    operations = [
        migrations.AddField(
            model_name='node',
            name='is_title',
            field=models.BooleanField(default=False),
        ),
    ]
