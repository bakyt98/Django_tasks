from rest_framework import serializers
from .models import Car, MainUser
from django.contrib.auth.models import User


class UserTestSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class UserTestSerializer2(serializers.ModelSerializer):
    class Meta:
        model = MainUser
        fields = '__all__'


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'
