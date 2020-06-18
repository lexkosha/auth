from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class UserProfile(models.Model):
    age = models.IntegerField()
    country = models.CharField(max_length=150, verbose_name='Страна', null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.PROTECT,
                                related_name='profile')

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

