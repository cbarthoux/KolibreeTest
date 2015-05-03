# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dentistsApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dentist',
            name='patients_list',
        ),
        migrations.AddField(
            model_name='user',
            name='dentist',
            field=models.ForeignKey(default=None, to='dentistsApp.Dentist'),
        ),
    ]
