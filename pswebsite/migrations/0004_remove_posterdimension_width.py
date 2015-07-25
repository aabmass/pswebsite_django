# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pswebsite', '0003_posterdimension_height'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posterdimension',
            name='width',
        ),
    ]
