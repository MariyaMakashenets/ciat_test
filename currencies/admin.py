# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Currencies, CurrenciasHistory

admin.site.register(Currencies)
admin.site.register(CurrenciasHistory)


