from django import forms
#from django.contrib.auth.models import User
from .models import CustomUser


class UserCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'phone', 'first_name', 'last_name']
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password") 

        if password != confirm_password:
            raise forms.ValidationError("password do not match")
        
    def save(self, commit = True):
        User =  super().save(commit=False)
        User.set_password(self.cleaned_data["password"])
        if commit:
            User.save()
        return User    

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput) 

