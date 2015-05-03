# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dentistsApp', '0005_remove_user_dentist'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='dentist',
            field=models.ForeignKey(default=None, to='dentistsApp.Dentist'),
        ),
    ]
