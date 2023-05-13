from django import forms
from .models import Book
from django.contrib.auth.models import User

#DataFlair
class BookCreate(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
class AdminSigupForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']