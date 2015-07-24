# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('pswebsite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='posterdimension',
            name='units',
            field=models.CharField(choices=[('in', 'Inches'), ('cm', 'Centimeters')], max_length=10, default='in'),
        ),
        migrations.AlterField(
            model_name='poster',
            name='user_creator',
            field=models.ForeignKey(verbose_name='the user that created this product', editable=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
