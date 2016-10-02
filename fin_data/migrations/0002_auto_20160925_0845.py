# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-25 08:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fin_data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FinanceDataId',
            fields=[
                ('stock_id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='financedataitem',
            name='stock_id',
        ),
        migrations.AddField(
            model_name='financedataitem',
            name='id',
            field=models.AutoField(auto_created=True, default=12, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='financedataitem',
            name='stock',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fin_data.FinanceDataId'),
        ),
    ]