from django.contrib import admin

# Register your models here.
from .models import Company

@admin.register(Company)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'address', 'phone',]
