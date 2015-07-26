# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pswebsite', '0005_auto_20150725_2130'),
    ]

    operations = [
        migrations.AddField(
            model_name='poster',
            name='tagline',
            field=models.TextField(default='One time only default tagline here'),
            preserve_default=False,
        ),
    ]
