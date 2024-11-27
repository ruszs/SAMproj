from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'year_level', 'program_course')
    search_fields = ('name', 'email', 'program_course')
    list_filter = ('year_level',)
