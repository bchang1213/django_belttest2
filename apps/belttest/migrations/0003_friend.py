# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-29 00:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('belttest', '0002_auto_20170929_0001'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('friend', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friendee', to='belttest.User')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friender', to='belttest.User')),
            ],
        ),
    ]
