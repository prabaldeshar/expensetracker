from django.contrib import admin
from .models import Transcation, Income, Expense

# Register your models here.
# admin.site.register(Person)
admin.site.register(Transcation)
admin.site.register(Income)
admin.site.register(Expense)
