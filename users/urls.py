from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('signup/', views.signup, name="signup"),
    path('login/', views.login_user, name="login_user"),
    path('home/add_income/<int:user_id>/', views.add_income, name="add_income"),
]