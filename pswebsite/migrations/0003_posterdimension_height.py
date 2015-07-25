# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pswebsite', '0002_auto_20150724_0523'),
    ]

    operations = [
        migrations.AddField(
            model_name='posterdimension',
            name='height',
            field=models.PositiveSmallIntegerField(verbose_name='height along vertical', default=20, help_text='Height along the vertical side of a poster'),
            preserve_default=False,
        ),
    ]
