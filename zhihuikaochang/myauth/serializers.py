from .models import User
from rest_framework import serializers


class UserRegisterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('uid', 'phone.', 'email', 'password')


class UserLoginSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('uid', 'password')