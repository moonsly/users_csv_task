# -*- coding: utf-8 -*-
""" extra template tags - eligible age >13 and bizzfuzz """

from django import template
from datetime import datetime, timedelta

from exos_task.utils import yearsago, OLDER_THEN_YEARS

register = template.Library()


@register.filter
def is_allowed(value):
    """ is age > 13 """
    if not value:
        return "blocked"
    birthdate = datetime.combine(value, datetime.min.time())
    # datetime.strptime(value, "%B %d, %Y")
    if birthdate <= yearsago(OLDER_THEN_YEARS):
        return "allowed"
    else:
        return "blocked"


@register.filter
def bizzfuzz(value):
    """ multiples 3 = +Bizz, multiples 5 += Fuzz """
    value = int(value)
    res = ""
    if value % 3 == 0:
        res += "Bizz"
    if value % 5 == 0:
        res += "Fuzz"
    
    if not res:
        res = value
    return res