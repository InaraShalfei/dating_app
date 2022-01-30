import os
import smtplib
from email.mime.text import MIMEText

from django_filters.rest_framework import DjangoFilterBackend
from dotenv import load_dotenv
from rest_framework import status, viewsets, filters
from rest_framework.decorators import action
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from users.filters import UserSetFilter
from users.models import CustomUser, UserFollow
from users.serializers import CustomUserSerializer, UserListSerializer

load_dotenv()


def send_message(follower, followed):
    msg = MIMEText(
        f'Вы понравились {followed.first_name}!'
        f' Почта участника: {followed.email}')
    msg['Subject'] = 'Вы понравились!'
    msg['From'] = os.getenv('SMTP_LOGIN')
    msg['To'] = follower.email
    server = smtplib.SMTP(os.getenv('SMTP_HOST'), os.getenv('SMTP_PORT'))
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(msg['From'], os.getenv('SMTP_PASSWORD'))
    server.sendmail(msg['From'], [msg['To']], msg.as_string())
    server.quit()


class CustomRegistrationView(viewsets.ModelViewSet):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()

    @action(detail=False, methods=['post'], url_path='create',
            permission_classes=AllowAny)
    def create(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'], url_path='match',
            permission_classes=IsAuthenticated)
    def match(self, request, id):
        followed = CustomUser.objects.get(id=id)
        match_1, _ = UserFollow.objects.get_or_create(follower=request.user,
                                                      followed=followed)
        match_2 = UserFollow.objects.filter(follower__id=id,
                                            followed=request.user).first()
        if match_1 and match_2:
            send_message(match_1.follower, match_1.followed)
            send_message(match_2.follower, match_2.followed)
            return Response({'email': match_1.followed.email})
        return Response()


class UserSet(ListAPIView):
    serializer_class = UserListSerializer
    queryset = CustomUser.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_class = UserSetFilter
