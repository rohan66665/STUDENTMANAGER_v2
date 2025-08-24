from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'course')

from django.contrib.admin.sites import site

if not site.is_registered(Student):
    admin.site.register(Student, StudentAdmin)
