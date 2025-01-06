from djoser.serializers import UserCreateSerializer, UserSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class CustomUserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'username', 'email', 'password', 're_password', 'first_name', 'last_name')

class CustomUserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')

class CustomSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150, help_text="Имя пользователя")
    email = serializers.EmailField(help_text="Адрес электронной почты")


