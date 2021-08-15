from django.contrib import admin
from .models import Menu ,Contact
# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display=('name','email','number')

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display=('category','food_name','price')

