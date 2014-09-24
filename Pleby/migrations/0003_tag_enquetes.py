# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Pleby', '0002_usuario_especial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='enquetes',
            field=models.ManyToManyField(to='Pleby.Enquete', verbose_name=b'enquetes'),
            preserve_default=True,
        ),
    ]
