from random import randint

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator


class MyUser(AbstractUser):
    birthday = models.DateField(blank=False)
    random_number = models.PositiveIntegerField(blank=False, validators=[
        MaxValueValidator(100),
        MinValueValidator(1)
    ])

    def save(self, *args, **kwargs):
        # -- handle extra kwargs on create
        for fld in ("birthday", "random_number"):
            if fld in kwargs:
                setattr(self, fld, kwargs[fld])

        # -- generate random_number
        if not self.random_number:
            self.random_number = randint(1, 100)
        super(MyUser, self).save(*args, **kwargs)