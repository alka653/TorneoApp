# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-15 15:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inscripcion', '0003_auto_20170305_1931'),
    ]

    operations = [
        migrations.AddField(
            model_name='inscritos',
            name='telefono',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]
