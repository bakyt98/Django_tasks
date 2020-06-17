from rest_framework import serializers
from .models import UserTest, Car


class UserTestSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()


class UserTestSerializer2(serializers.ModelSerializer):
    class Meta:
        model = UserTest
        fields = '__all__'


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'
