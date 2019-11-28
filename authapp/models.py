from django.contrib.auth.models import AbstractUser
from django.db import models


class ShopUser(AbstractUser):
    age = models.PositiveSmallIntegerField(verbose_name='возраст')
    avatar = models.ImageField(upload_to='user_avatar', blank=True)

