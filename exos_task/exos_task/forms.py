# -*- coding: utf-8 -*-

from django.forms import ModelForm
from django import forms

from exos_task.models import MyUser


class SaveUserForm(ModelForm):

    class Meta:
        model = MyUser
        fields = ('username', 'email', 'birthday', 'random_number',)


    def clean_random_number(self):
        value = int(self.cleaned_data.get('random_number'))
        if value > 100 or value < 1:
            raise forms.ValidationError("Enter number between 1 and 100")

        return value
