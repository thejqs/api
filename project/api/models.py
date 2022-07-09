from django.conf import settings
from django.core.cache import cache
from django.db import models
from django.db.models.signals import post_save


class Sprocket(models.Model):
    teeth = models.PositiveIntegerField(null=False, blank=False)
    outside_diameter = models.PositiveIntegerField(null=False, blank=False)
    pitch = models.PositiveIntegerField(null=False, blank=False)
    pitch_diameter = models.PositiveIntegerField(null=False, blank=False)

class Factory(models.Model):
    chart_data = models.JSONField(null=False, blank=False)
