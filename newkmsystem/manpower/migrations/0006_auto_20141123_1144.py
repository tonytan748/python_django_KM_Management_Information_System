# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manpower', '0005_auto_20141123_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manpower',
            name='working_time',
            field=models.CharField(max_length=120),
            preserve_default=True,
        ),
    ]
