# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manpower', '0006_auto_20141123_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manpower',
            name='time_in',
            field=models.CharField(max_length=30),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='manpower',
            name='time_out',
            field=models.CharField(max_length=30),
            preserve_default=True,
        ),
    ]
