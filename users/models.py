from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from users.managers import CustomUserManager


class CustomUser(AbstractUser):
    class Gender(models.TextChoices):
        FEMALE = 'female'
        MALE = 'male'

    avatar = models.ImageField(upload_to='avatars/', blank=False)
    gender = models.CharField(choices=Gender.choices, max_length=200)
    first_name = models.CharField(max_length=150, blank=False)
    last_name = models.CharField(max_length=150, blank=False)
    email = models.EmailField(blank=False, unique=True)
    longitude = models.FloatField(blank=False, validators=[
        MinValueValidator(-180.0), MaxValueValidator(180.0)
    ])
    latitude = models.FloatField(blank=False, validators=[
        MinValueValidator(-90.0), MaxValueValidator(90.0)
    ])
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'avatar', 'gender',
                       'longitude', 'latitude']

    class Meta:
        ordering = ('first_name', 'last_name',)
        verbose_name = 'user'
        verbose_name_plural = 'users'

    objects = CustomUserManager()

    def __str__(self):
        return self.get_full_name()


class UserFollow(models.Model):
    follower = models.ForeignKey(CustomUser, on_delete=models.CASCADE,
                                 related_name='user_following')
    followed = models.ForeignKey(CustomUser, on_delete=models.CASCADE,
                                 related_name='user_followed')

    class Meta:
        verbose_name = 'Following user'
        verbose_name_plural = 'Following users'
        constraints = [
            models.UniqueConstraint(
                fields=['follower', 'followed'],
                name='unique_following'
            )
        ]
