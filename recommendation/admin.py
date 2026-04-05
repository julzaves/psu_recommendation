from django.contrib import admin
from .models import College, PSUProgram

@admin.register(College)
class CollegeAdmin(admin.ModelAdmin):
    list_display = ['name', 'abbreviation', 'dean']
    list_filter = ['name']
    search_fields = ['name', 'abbreviation']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(PSUProgram)
class PSUProgramAdmin(admin.ModelAdmin):
    list_display = ['name', 'college', 'degree_level', 'duration_years', 'ideal_skills', 'ideal_interests', 'is_active']
    list_filter = ['college', 'degree_level', 'duration_years', 'is_active']
    search_fields = ['name', 'description']
    list_editable = ['is_active']
    raw_id_fields = ['college']