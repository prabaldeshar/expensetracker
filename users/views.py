from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import HttpResponse
from .forms import LoginForm, CreateUserForm, AddIncomeForm, AddExpenseForm
from django.views.decorators.cache import never_cache
from . import urls

# Create your views here.

def home(response):
    users = User.objects.all()
    data = {'users': users}
    return render(response, 'users/home.html', data)

def signup(response):
    form = CreateUserForm()
    if response.method == "POST":
        form = CreateUserForm(response.POST or None)
        print(form)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = CreateUserForm()
        
    return render(response, 'users/signup.html', {"form":form})

@never_cache
def login_user(response):
    # if response.user.is_authenticated:
    #     return HttpResponseRedirect(reverse('/home'))
    
    if response.method == 'POST':
        form = LoginForm(response.POST or None)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']   
            user = authenticate(response, username=username, password=password)
            print(user)
            if user:
                login(response, user)
                return redirect("home")
            else:
                messages.error(response, 'Invalid username or password')
        
        else: 
            messages.error(response, 'Invalid Form')
        
    else:
        form = LoginForm()
    
    return render(response, 'users/login.html', {"form": form})

def add_income(response, user_id):
    form = AddIncomeForm()
    current_user = User.objects.get(id=user_id)
    if response.method == 'POST':
        form = AddIncomeForm(response.POST or None)
        form.instance.user = current_user
        if form.is_valid():=
           form.save()
           return redirect("home") 
        else:
            messages.error(response, 'Invalid Form')
    
    else:
        form = AddIncomeForm()
    
    return render(response, 'users/home.html', {"form": form})
    


