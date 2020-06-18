from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class UserProfile(models.Model):
    age = models.IntegerField()
    user = models.OneToOneField(User, on_delete=models.PROTECT,
                                related_name='profile')

    class Meta:
        verbose_name='Профиль'
        verbose_name_plural='Профили'

    def __str__(self):
        return self.user