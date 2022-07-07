# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-17 23:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True
    operations = [
        migrations.CreateModel(
            name="Sprocket",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("teeth", models.PositiveIntegerField(null=False, blank=False)),
                ("outside_diameter", models.PositiveIntegerField(null=False, blank=False)),
                ("pitch", models.PositiveIntegerField(null=False, blank=False)),
                ("pitch_diameter", models.PositiveIntegerField(null=False, blank=False)),
            ],
        ),
        migrations.CreateModel(
            name="Factory",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("chart_data", models.JSONField(null=False, blank=False)),
            ]
        ),
    ]
