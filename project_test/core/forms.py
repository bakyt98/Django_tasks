from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import MainUser


class MainUserCreationForm(UserCreationForm):
    """
    Creation form for user in admin.

    ...

    Methods
    -------
    __init__(self, *args, **kwargs)
        function which will be done when starts to load the creation of user page
    """

    def __init__(self, *args, **kwargs):
        """
        In creation of user the password fields will not be required and will not autocomplete.
        """
        super(MainUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].required = False
        self.fields['password2'].required = False
        # If one field gets autocompleted but not the other, our 'neither
        # password or both password' validation will be triggered.
        self.fields['password1'].widget.attrs['autocomplete'] = 'off'
        self.fields['password2'].widget.attrs['autocomplete'] = 'off'

    class Meta(UserCreationForm.Meta):
        model = MainUser
        fields = '__all__'


class MainUserChangeForm(UserChangeForm):
    """
    Form to change user in admin panel.

    ...

    Methods
    -------
    __init__(self, *args, **kwargs)
        function which will be done when starts to load the change user page
    """

    def __init__(self, *args, **kwargs):
        super(MainUserChangeForm, self).__init__(*args, **kwargs)

    class Meta(UserChangeForm.Meta):
        model = MainUser
        fields = '__all__'
