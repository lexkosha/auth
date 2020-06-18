from django import forms
from .models import UserProfile

class ProfileCreationForm(forms.ModelForm):

    class Meta:
        models = UserProfile
        fields = ['age']