# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-29 09:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20171015_0331'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CommentReport',
            new_name='ReportComment',
        ),
        migrations.AlterModelOptions(
            name='school',
            options={'ordering': ['school_name']},
        ),
    ]
