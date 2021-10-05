from django import forms
#from django.contrib.auth.forms import UserCreationForm
from accounts.models import ManagerModel
from django.contrib.auth.forms import AuthenticationForm

class ManagerRegistrationForm(forms.ModelForm):
    class Meta:
        model = ManagerModel
        exclude = ['last_login']

class LoginForm(AuthenticationForm):
    username = forms.EmailField(label='Email')
    