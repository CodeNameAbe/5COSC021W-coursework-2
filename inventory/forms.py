from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . models import MainInventory, Type

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class MainInventoryForm(forms.ModelForm):
    type = forms.ModelChoiceField(queryset=Type.objects.all(), initial=0)
    class Meta:
        model = MainInventory
        fields = '__all__'
