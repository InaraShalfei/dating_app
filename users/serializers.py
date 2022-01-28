from django.db import IntegrityError
from djoser.serializers import UserCreateSerializer

from users.models import CustomUser


class CustomUserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = CustomUser
        fields = tuple(CustomUser.REQUIRED_FIELDS) + ('password', 'email')





