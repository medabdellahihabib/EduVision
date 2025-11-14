from django.contrib import admin
from .models import School, Classroom

@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'email', 'phone', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('name', 'code', 'email')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'school', 'capacity', 'is_active')
    list_filter = ('school', 'is_active')
    search_fields = ('name', 'code', 'school__name')