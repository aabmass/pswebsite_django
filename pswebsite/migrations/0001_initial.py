# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Poster',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PosterDimension',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('length', models.PositiveSmallIntegerField(help_text='Length along the bottom of a poster', verbose_name='length along horizontal')),
                ('width', models.PositiveSmallIntegerField(help_text='Length along the vertical side of a poster', verbose_name='length along vertical')),
            ],
        ),
        migrations.CreateModel(
            name='PosterImage',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('image', models.ImageField(upload_to='productimages')),
                ('poster', models.ForeignKey(to='pswebsite.Poster')),
            ],
        ),
        migrations.AddField(
            model_name='poster',
            name='dimension',
            field=models.ManyToManyField(to='pswebsite.PosterDimension'),
        ),
        migrations.AddField(
            model_name='poster',
            name='user_creator',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='the user that created this product'),
        ),
    ]
