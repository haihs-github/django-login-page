from django import forms
from .models import User

class UserForm(forms.ModelForm): # chuyển form sang model tương ứng
    class Meta:
        model = User
        fields = ['username','password']