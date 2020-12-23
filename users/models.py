from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class Person(models.Model):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     email = models.EmailField()

#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"

class Transcation(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    income = models.IntegerField()
    expenditure = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Income(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField()
    source = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.source

class Expense(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField()
    purpose = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.purpose