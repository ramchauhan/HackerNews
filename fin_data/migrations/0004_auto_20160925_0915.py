# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-25 09:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fin_data', '0003_auto_20160925_0908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='financedataid',
            name='stock_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
