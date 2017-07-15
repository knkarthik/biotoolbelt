# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-05 14:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Input',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inputseq', models.TextField(help_text='Paste your DNA sequence in FASTA format')),
            ],
        ),
    ]
