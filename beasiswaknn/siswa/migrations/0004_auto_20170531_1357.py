# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-31 13:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siswa', '0003_auto_20170531_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siswabaru',
            name='x1',
            field=models.CharField(choices=[(b'1', b'Ada'), (b'0', b'Tidak Ada')], max_length=10),
        ),
    ]
