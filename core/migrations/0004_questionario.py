# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-25 17:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20171125_1526'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questionario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acertos', models.CharField(max_length=5)),
            ],
        ),
    ]
