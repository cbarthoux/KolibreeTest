# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dentistsApp', '0002_auto_20150502_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='dentist',
            field=models.ForeignKey(to='dentistsApp.Dentist'),
        ),
    ]
