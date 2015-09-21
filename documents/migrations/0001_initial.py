# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=1024)),
                ('parent_document', models.ForeignKey(blank=True, to='documents.Document', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField()),
                ('order', models.IntegerField(default=1)),
                ('numbering_type', models.CharField(default=b'none', max_length=255, choices=[(b'numbers', 'Numbers'), (b'roman', 'Roman numbers'), (b'letters', 'Letters'), (b'none', 'No numbering')])),
                ('numbering_format', models.CharField(default=b'%%s', max_length=255)),
                ('document', models.ForeignKey(related_name='nodes', to='documents.Document')),
                ('parent_node', models.ForeignKey(related_name='child_nodes', blank=True, to='documents.Node', null=True)),
            ],
        ),
    ]
