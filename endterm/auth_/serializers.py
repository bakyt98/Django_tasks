from rest_framework import serializers
from django.contrib.auth.hashers import check_password
from auth_.models import MainUser
from auth_.token import get_token
import logging

logger = logging.getLogger(__name__)

class MainUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainUser
        fields = ('username', 'password')
        write_only_fields = ('password',)

    def create(self, validated_data):
        return MainUser.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=200)
    password = serializers.CharField(max_length=200)

    def validate(self, attrs):
        logger.info('validating login of user')
        try:
            user = MainUser.objects.get(username=attrs['username'])
        except:
            logger.error('login failed, user does not exist with this username: {}'.format(attrs['username']))
            raise serializers.ValidationError('User dooes not exist')
        if not user.check_password(attrs['password']):
            logger.error('password is not correct')
            raise serializers.ValidationError('Useer does not exist')
        attrs['user'] = user
        return attrs

    def login(self):
        user = self.validated_data['user']
        token = get_token(user)
        return user, token


