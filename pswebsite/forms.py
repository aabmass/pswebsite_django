from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']

    def save(self, commit=True):
        user = super().save(False)
        
        # username and email are the same in this scheme. Enforce it!
        user.username = user.email
        
        if commit:
            user.save()
        return user
