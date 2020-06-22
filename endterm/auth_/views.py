from django.shortcuts import render
from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.decorators import action

from auth_.models import MainUser
from auth_.serializers import MainUserSerializer, LoginSerializer


class MainUserViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = MainUser.objects.all()
    # http_method_names = ['post']
    permission_classes = (AllowAny,)

    def get_serializer_class(self):
        if self.action == 'login':
            return LoginSerializer
        return MainUserSerializer

    @action(methods=['GET'], detail=False)
    def login(self, request):
        serializer = self.get_serializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.login()
        return Response({'user': MainUserSerializer(user).data,
                         'token': token})
