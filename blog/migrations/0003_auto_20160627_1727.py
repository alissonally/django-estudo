# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-27 20:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20160627_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_slug',
            field=models.SlugField(verbose_name='Slug'),
        ),
    ]