from django.forms import ModelForm
from .models import Status, Pro
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class StatusForm(ModelForm):
    class Meta:
        model = Status
        fields = ['date', 'status']


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    # Configuration
    class Meta:
        model = User
        fields = ['username', 'email','first_name','last_name', 'password1', 'password2']


# Create a UserUpdateForm to update username and email
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

# Create a ProfileUpdateForm to update image
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Pro
        fields = ['image', 'experience', 'goals']
