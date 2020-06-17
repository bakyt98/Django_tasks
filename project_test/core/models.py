from django.db import models


# Create your models here.

class UserTestManager(models.Manager):

    def get_users_by_first_name(self, string):
        users = UserTest.objects.filter(first_name__contains=string)
        return users


class UserTest(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    objects = UserTestManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
        # return "{} {}".format(self.first_name, self.last_name)

    def get_cars(self):
        return self.car_users.all()


class Auto(models.Model):
    RED = "RED"
    BLACK = "BLACK"
    WHITE = "WHITE"
    colors = (
        (RED, "Красный"),
        (BLACK, "Черный"),
        (WHITE, "Белый")
    )
    model = models.CharField(max_length=200, blank=True, null=True)
    color = models.CharField(max_length=100, choices=colors,
                             default=BLACK)

    class Meta:
        abstract = True


class Car(Auto):
    name = models.CharField(max_length=200, verbose_name="Название",
                            unique=True)
    price = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Авто"
        verbose_name_plural = "Автомашины"

    def drive(self):
        return f"{self.name} is driving"


class Bus(Auto):
    TYPE1 = "TYPE1"
    TYPE2 = "TYPE2"
    types = (
        (TYPE1, TYPE1),
        (TYPE2, TYPE2)
    )
    type = models.CharField(max_length=100, choices=types,
                            default=TYPE1)
    amount_passengers = models.PositiveIntegerField(default=0)


class CarUser(models.Model):
    user = models.ForeignKey(UserTest, on_delete=models.CASCADE,
                             related_name='car_users')
    car = models.ForeignKey(Car, on_delete=models.CASCADE,
                            related_name='car_users')
