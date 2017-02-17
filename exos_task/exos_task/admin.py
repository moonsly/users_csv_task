# -*- coding: utf-8 -*-
""" administration config for Task """
from django.contrib import admin
from django.conf.locale.ru import formats as ru_formats
from exos_task.models import MyUser

ru_formats.DATETIME_FORMAT = "d.m.Y H:i:s"


class UserAdmin(admin.ModelAdmin):
    """ Task admin module """
    search_fields = ('id', )
    list_display = (
        'id',
        'username',
        'email',
        'birthday',
        'random_number',
    )

admin.site.register(MyUser, UserAdmin)
