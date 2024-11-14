from django import forms
from .models import LoginAttempt

class LoginAttemptForm(forms.ModelForm):
    class Meta:
        model = LoginAttempt
        fields = ['name', 'email']  
