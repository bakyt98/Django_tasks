from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .forms import MainUserChangeForm, MainUserCreationForm
from .models import Car, CarUser, MainUser

# Register your models here.
# admin.site.register(Car)

admin.site.register(CarUser)
# admin.site.register(UserTest)
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'model', 'name', 'price', 'color')
    list_filter = ('color',)
    search_fields = ('name', 'model')

# if use User model from django
# admin.site.unregister(User)

# @admin.register(User)
# class UserAdmin(UserAdmin):
#     list_display = ('id', 'username')

# if extends from AbstractBaseUser and PermissionsMixin
@admin.register(MainUser)
class UserAdmin(UserAdmin):
    form = MainUserChangeForm
    add_form = MainUserCreationForm
    list_display = ('id', 'email')
    list_filter = ('is_superuser',)
    fieldsets = (
        ('Main Fields', dict(fields=(
            'email',
            'full_name',
        ))
        ),
        ('Password', {'fields': ('password',)}),
        ('Permissions',
         {'fields': ('groups', 'is_staff', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
         ),
    )
    ordering = ['email']
    search_fields = ['email']
