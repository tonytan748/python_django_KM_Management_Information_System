# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manpower', '0003_auto_20141120_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manpower',
            name='shift',
            field=models.ForeignKey(to='manpower.Shift'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='code',
            field=models.CharField(max_length=5),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='salary',
            name='employee',
            field=models.ForeignKey(to='manpower.Employee', unique=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='shift',
            name='name',
            field=models.CharField(unique=True, max_length=100),
            preserve_default=True,
        ),
    ]
