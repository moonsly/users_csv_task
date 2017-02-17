# -*- coding: utf-8 -*-
import re
from datetime import datetime, timedelta

from django.test import TestCase, Client, modify_settings
from django import forms

from exos_task.models import MyUser
from exos_task.utils import yearsago, OLDER_THEN_YEARS


def check_regex(content, values):
    regex_tmpl = r'<tr>.*?<td>.*?{}.*?</td>.*?<td>{}</td>.*?<td>{}</td>.*?</tr>'
    # print("ALKSJDLFKJ", regex_tmpl.format(*values))
    regex = re.compile(regex_tmpl.format(*values), re.DOTALL)
    return bool(regex.search(content))


class MainTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up data for the whole TestCase
        birthday = yearsago(OLDER_THEN_YEARS)
        cls.admin = MyUser.objects.create(username="admin", random_number=15,
                                          birthday=yearsago(OLDER_THEN_YEARS))

        # add users with border conditions for template tags
        birthday_plus_day = yearsago(OLDER_THEN_YEARS) + timedelta(days=1)
        MyUser.objects.create(username="user1", birthday=birthday_plus_day, random_number=34)

        birthday_minus_day = yearsago(OLDER_THEN_YEARS) - timedelta(days=-1)
        MyUser.objects.create(username="user2", birthday=birthday_minus_day, random_number=36)

        # bizz fuzz borders
        MyUser.objects.create(username="user3", birthday=birthday, random_number=3)
        MyUser.objects.create(username="user4", birthday=birthday, random_number=4)
        MyUser.objects.create(username="user5", birthday=birthday, random_number=5)

        cls.client = Client()


    def test1_birthdays_bizzfuzz(self):
        # test correct work of Eligible/is_allowed template tag
        resp = self.client.get('/users/')
        assert resp.status_code == 200 and len(resp.content)

        content = resp.content
        assert check_regex(content, ["admin", "allowed", "BizzFuzz"])

        assert check_regex(content, ["user1", "blocked", "34"])
        assert check_regex(content, ["user2", "allowed", "Bizz"])
        assert check_regex(content, ["user3", "allowed", "Bizz"])
        assert check_regex(content, ["user4", "allowed", "4"])
        assert check_regex(content, ["user5", "allowed", "Fuzz"])


    def test2_incorrect_date(self):
        try:
            MyUser.objects.create(username="user123", birthday=123, random_number=5)
        except TypeError:
            assert True
        else:
            assert False


    def test3_incorrect_date_format(self):
        try:
            MyUser.objects.create(username="user23", birthday="1958-01-", random_number=5)
        except forms.ValidationError:
            assert True
        else:
            assert False