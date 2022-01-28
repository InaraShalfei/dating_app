import random
import string

from PIL import Image
from djoser.serializers import UserCreateSerializer

from dating_app.settings import MEDIA_ROOT
from users.models import CustomUser


def watermark_image(file):
    image = Image.open(file)
    watermarked_image = Image.open(MEDIA_ROOT + '/watermark.jpg')
    watermarked_image = watermarked_image.resize(image.size, Image.NEAREST)
    my_img = Image.blend(image, watermarked_image, 0.5)
    filename_prefix = ''.join(random.choices(string.ascii_uppercase, k=16))
    new_filename = f'/avatars/{filename_prefix}-{file.name}'
    my_img.save(MEDIA_ROOT + new_filename)

    return new_filename


class CustomUserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = CustomUser
        fields = tuple(CustomUser.REQUIRED_FIELDS) + ('password', 'email')

    def create(self, validated_data):
        avatar = validated_data.pop('avatar')
        avatar = watermark_image(avatar)
        validated_data['avatar'] = avatar
        return super().create(validated_data)
