from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Income, Expense

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name','last_name', 'email','password']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class AddIncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['amount', 'source']

class AddExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['amount', 'purpose']
