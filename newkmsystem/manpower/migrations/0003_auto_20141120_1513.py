# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manpower', '0002_shift'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manpower',
            name='working_time',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
    ]
