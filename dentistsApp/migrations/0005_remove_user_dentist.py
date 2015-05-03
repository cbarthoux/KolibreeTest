# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dentistsApp', '0004_auto_20150502_1950'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='dentist',
        ),
    ]
