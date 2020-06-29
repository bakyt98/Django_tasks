"""
File of description of classes
"""
from django.db import models
from django.contrib.auth.models import User, AbstractUser, AbstractBaseUser, PermissionsMixin, BaseUserManager


class MainUserManager(BaseUserManager):
    """
        Main user manager

        Methods
        -------
        create_user(self, username, password=None, full_name=None, email=None)
            creates user with params
    """

    def create_user(self, username, password=None, full_name=None, email=None):
        """
        Creates user
        :param username: username of user
        :type username: str
        :return: instance of user

        Attributes
        ----------
        username: str
            username of user
        """
        if not username:
            raise ValueError('User must have a username')
        user = self.model(username=username, email=email, full_name=full_name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        """
        Creates and saves a superuser with the given email and password
        """
        user = self.model(username=username)
        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class MainUser(AbstractBaseUser, PermissionsMixin):
    """
    Class describes user instance

    Attributes
    ----------
    username: str
        username of user

    Methods
    -------
    name_ofmethod()
        what it does
    """
    username = models.CharField(max_length=200, unique=True)
    email = models.EmailField(max_length=300, unique=True)
    full_name = models.CharField(max_length=200)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'

    objects = MainUserManager()


class Profile(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.ForeignKey(MainUser, on_delete=models.CASCADE)
    age = models.PositiveIntegerField()
    bio = models.TextField()



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
    # user = models.ForeignKey(User, on_delete=models.CASCADE,
    #                          related_name='car_users')
    user = models.ForeignKey(MainUser, on_delete=models.CASCADE,
                             related_name='car_users')
    car = models.ForeignKey(Car, on_delete=models.CASCADE,
                            related_name='car_users')
