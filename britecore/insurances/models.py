# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

import eav

class RiskType(models.Model):
    name = models.CharField(max_length=50, unique=True)
    attributes = models.ManyToManyField(eav.models.Attribute)

    def __str__(self):
        return self.name

class Risk(models.Model):
    name = models.CharField(max_length=50)
    type = models.ForeignKey(RiskType, related_name="risks")

eav.register(Risk)