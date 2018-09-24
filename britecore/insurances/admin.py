# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from eav.forms import BaseDynamicEntityForm
from eav.admin import BaseEntityAdmin

from .models import Risk, RiskType

class RiskAdminForm(BaseDynamicEntityForm):
    model = Risk

class RiskAdmin(BaseEntityAdmin):
    form = RiskAdminForm

admin.site.register(Risk, RiskAdmin)
admin.site.register(RiskType)