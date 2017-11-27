# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-27 06:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('analytics', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Urls',
            fields=[
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('url_title', models.TextField(default='')),
                ('long_url', models.URLField()),
                ('analytics', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='analytics.Analytics')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_links', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Urls',
            },
        ),
    ]