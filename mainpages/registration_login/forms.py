from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput
#from .models import Profile

#Create User (Model Form)
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# Authenicate a user (Model Form)
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

"""
# Create UserDetailsForm
class UserDetailsForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Enter your first name')
    last_name = forms.CharField(max_length=30, required=True, help_text='Enter your last name')

    class Meta:
        model = Profile
        fields = ['address', 'contact_number']

    def save(self, user=None, commit=True):
        profile = super(UserDetailsForm, self).save(commit=False)
        if user:
            user.first_name = self.cleaned_data['first_name']
            user.last_name = self.cleaned_data['last_name']
            user.save()
            profile.user = user
        if commit:
            profile.save()
        return profile
"""