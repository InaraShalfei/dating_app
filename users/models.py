from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    class Gender(models.TextChoices):
        FEMALE = 'female'
        MALE = 'male'

    avatar = models.ImageField(upload_to='media/', blank=True, null=True)
    gender = models.CharField(choices=Gender.choices, max_length=200)
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name', 'avatar', 'gender']

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        return self.first_name + self.last_name
