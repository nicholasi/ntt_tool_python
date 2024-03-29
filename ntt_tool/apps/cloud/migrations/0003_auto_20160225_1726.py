# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-25 17:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cloud', '0002_auto_20160225_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cloudtraffictenants',
            name='cloud_traffic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cloud_traffic_tenants', to='cloud.CloudTraffic'),
        ),
        migrations.AlterField(
            model_name='cloudtraffictenants',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cloud_traffic_tenants_creator', to=settings.AUTH_USER_MODEL),
        ),
    ]
