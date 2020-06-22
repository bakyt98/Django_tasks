from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser,
                                        PermissionsMixin)
from utils import constants


class MainUserManager(BaseUserManager):
    """
    Main user manager
    """

    def create_user(self, username, password=None):
        """
        Creates and saves a user with the given username.
        """
        if not username:
            raise ValueError('User must have a username')
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        """
        Creates and saves a superuser with the given phone and password
        """
        user = self.create_user(username=username, password=password)
        user.is_admin = True
        user.is_superuser = True
        user.is_moderator = True
        user.is_staff = True
        user.role = constants.ADMIN
        user.save(using=self._db)
        return user

class MainUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=200, unique=True)
    timestamp = models.DateTimeField(auto_now=True)
    role = models.CharField(max_length=100, choices=constants.ROLES, default=constants.GUEST)
    is_active = models.BooleanField(default=True, verbose_name='Активность')
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False, verbose_name='Сотрудник')
    objects = MainUserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username
