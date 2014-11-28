# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(unique=True, max_length=10)),
                ('name', models.CharField(unique=True, max_length=150)),
            ],
            options={
                'ordering': ['code'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Lend',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('payed_period', models.CharField(max_length=50, null=True, blank=True)),
                ('lend_desc', models.TextField()),
                ('lend_acount', models.DecimalField(default=0, max_digits=16, decimal_places=3)),
                ('additional_desc', models.TextField()),
                ('additional_acount', models.DecimalField(default=0, max_digits=16, decimal_places=3)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('create_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('employee', models.ForeignKey(to='manpower.Employee')),
            ],
            options={
                'ordering': ['-create_date'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ManPower',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time_in', models.DateTimeField()),
                ('time_out', models.DateTimeField()),
                ('lunch', models.IntegerField(default=1)),
                ('shift', models.CharField(max_length=2)),
                ('working_time', models.DecimalField(default=0, max_digits=16, decimal_places=3)),
                ('remark', models.TextField()),
                ('create_by', models.CharField(max_length=120)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('is_checked', models.BooleanField(default=False)),
                ('checked_by', models.CharField(max_length=200, null=True, blank=True)),
                ('checked_date', models.DateTimeField(auto_now_add=True)),
                ('time100', models.DecimalField(default=0, max_digits=16, decimal_places=3)),
                ('time100salary', models.DecimalField(default=0, max_digits=16, decimal_places=3)),
                ('time125', models.DecimalField(default=0, max_digits=16, decimal_places=3)),
                ('time125salary', models.DecimalField(default=0, max_digits=16, decimal_places=3)),
                ('time150', models.DecimalField(default=0, max_digits=16, decimal_places=3)),
                ('time150salary', models.DecimalField(default=0, max_digits=16, decimal_places=3)),
                ('time200', models.DecimalField(default=0, max_digits=16, decimal_places=3)),
                ('time200salary', models.DecimalField(default=0, max_digits=16, decimal_places=3)),
                ('timeremark', models.TextField()),
                ('is_payed', models.BooleanField(default=False)),
                ('payed_period', models.CharField(max_length=50, null=True, blank=True)),
                ('employee', models.ForeignKey(to='manpower.Employee')),
            ],
            options={
                'ordering': ['time_in'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(unique=True, max_length=5)),
                ('code_word', models.CharField(max_length=1)),
                ('rev', models.IntegerField(default=0)),
                ('name_1', models.CharField(max_length=150, blank=True)),
                ('name_2', models.CharField(max_length=300, blank=True)),
                ('payment', models.CharField(max_length=50, blank=True)),
                ('status', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['code'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('daily', models.DecimalField(default=0, max_digits=16, decimal_places=3)),
                ('ot125', models.DecimalField(default=0, max_digits=16, decimal_places=3)),
                ('ot150', models.DecimalField(default=0, max_digits=16, decimal_places=3)),
                ('ot200', models.DecimalField(default=0, max_digits=16, decimal_places=3)),
                ('morning', models.DecimalField(default=0, max_digits=16, decimal_places=3)),
                ('everyday', models.DecimalField(default=0, max_digits=16, decimal_places=3)),
                ('shift', models.CharField(max_length=50)),
                ('create_by', models.CharField(max_length=120)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('employee', models.ForeignKey(to='manpower.Employee')),
            ],
            options={
                'ordering': ['employee'],
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='manpower',
            name='project',
            field=models.ForeignKey(to='manpower.Project'),
            preserve_default=True,
        ),
    ]
