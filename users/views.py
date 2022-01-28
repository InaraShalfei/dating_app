from djoser import permissions
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from users.models import CustomUser
from users.serializers import CustomUserSerializer


class CustomRegistrationView(viewsets.ModelViewSet):
    # serializer_class = CustomUserSerializer
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()

    @action(detail=False, methods=['post'], url_path='create',  permission_classes=AllowAny)
    def create(self, request):
        if request.method == 'POST':
            serializer = CustomUserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
