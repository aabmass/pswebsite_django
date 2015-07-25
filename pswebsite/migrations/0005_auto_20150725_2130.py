# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pswebsite', '0004_remove_posterdimension_width'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poster',
            name='name',
            field=models.CharField(unique=True, max_length=100),
        ),
    ]
