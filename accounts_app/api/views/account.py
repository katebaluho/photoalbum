from django.contrib.auth.models import User
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet
from accounts_app.api.serializer.account import UserCreateSerializer


class UserCreateView(GenericViewSet, CreateModelMixin):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny, ]
