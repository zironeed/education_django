from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from users.models import User
from catalog.forms import StyleFormMixin


class UserForm(StyleFormMixin, UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')

