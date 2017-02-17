# -*- coding: utf-8 -*-
from datetime import datetime, timedelta


OLDER_THEN_YEARS = 13

def yearsago(years, from_date=None):
    """ helper function to get date N years ago """
    if from_date is None:
        from_date = datetime.now()
    try:
        return from_date.replace(year=from_date.year - years)
    except ValueError:
        # for 2/29!
        assert from_date.month == 2 and from_date.day == 29
        return from_date.replace(month=2, day=28,
                                 year=from_date.year-years)
