from django.contrib import admin
from .models import Student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['roll_no', 'name', 'school', 'classs', 'section', 'marks', 'address', 'picture']

admin.site.register(Student, StudentAdmin)