from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['skills', 'preferred_role', 'location']
        widgets = {
            'skills': forms.Textarea(attrs={'rows': 4}),
        }
