# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Pleby', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquete',
            name='data_ultima_votacao',
            field=models.DateField(null=True),
        ),
    ]
