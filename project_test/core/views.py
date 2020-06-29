from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


from .serializers import UserTestSerializer, UserTestSerializer2, \
    CarSerializer
from .models import Car, MainUser
from .token import get_token


@api_view(['POST'])
def create_user(request):
    serializer = UserTestSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = MainUser.objects.create_user(username=request.data['username'],
                                        email=request.data['email'],
                                        full_name=request.data['full_name'],
                                        password=request.data['password'])
    token = get_token(user)
    serializer2 = UserTestSerializer2(user)
    return Response({'token': token, 'user': serializer2.data})


@api_view(['GET'])
def get_all_users(request):
    users = UserTest.objects.all()
    serializer = UserTestSerializer2(users, many=True)
    return Response(serializer.data)


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = (IsAuthenticated,)


class CarViewSet2(viewsets.ReadOnlyModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarViewSet3(viewsets.GenericViewSet, mixins.CreateModelMixin,
                  mixins.ListModelMixin):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    @action(methods=['GET'], detail=True)
    def get_car_by_id(self, request, pk):
        car = Car.objects.get(id=pk)
        serializer = CarSerializer(car)
        return Response(serializer.data)
