from rest_framework import viewsets, mixins
from rest_framework.decorators import action

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import UserTestSerializer, UserTestSerializer2, \
    CarSerializer
from .models import UserTest, Car


@api_view(['POST'])
def create_user(request):
    serializer = UserTestSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = UserTest.objects.create(first_name=request.data['first_name'],
                                   last_name=request.data['last_name'])
    serializer2 = UserTestSerializer2(user)
    return Response(serializer2.data)


@api_view(['GET'])
def get_all_users(request):
    users = UserTest.objects.all()
    serializer = UserTestSerializer2(users, many=True)
    return Response(serializer.data)


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


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
