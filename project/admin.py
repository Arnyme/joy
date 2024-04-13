from django.contrib import admin
from .models import Project
from import_export.admin import ImportExportModelAdmin


class ProjectAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('project_name','image','created_at','updated_at')
    list_filter =('project_name','created_at')
    search_fields =('project_name','desription','created_at')
admin.site.register(Project, ProjectAdmin)



