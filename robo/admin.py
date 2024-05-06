from django.contrib import admin
from .models import Studenta
# Register your models here.

@admin.register(Studenta)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll', 'city']