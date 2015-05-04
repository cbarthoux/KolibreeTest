# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dentistsApp', '0006_user_dentist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='dentist',
            field=models.ForeignKey(to='dentistsApp.Dentist', null=True),
        ),
    ]
