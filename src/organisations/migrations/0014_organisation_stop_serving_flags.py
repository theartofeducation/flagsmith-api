# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-09-26 15:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organisations', '0013_organisation_alerted_over_plan_limit'),
    ]

    operations = [
        migrations.AddField(
            model_name='organisation',
            name='stop_serving_flags',
            field=models.BooleanField(default=False, help_text='Enable this to cease serving flags for this organisation.'),
        ),
    ]