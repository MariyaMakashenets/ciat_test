# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.utils import timezone
from datetime import datetime
from models import CurrenciasHistory

def all_currencies(request):
    last_curr = CurrenciasHistory.objects.filter(period__lte =datetime.today()).order_by('-period')
    context = {
        'ondate': datetime.today().strftime("%d/%m/%y"),
        'currency': '',
        'selling_rate': 0,
        'buying_rate': 0,
        'last_curr': last_curr,
    }
    return render(request, 'currencies/all_curr.html', context)


