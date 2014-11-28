# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manpower', '0004_auto_20141123_0304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manpower',
            name='working_time',
            field=models.FloatField(),
            preserve_default=True,
        ),
    ]
