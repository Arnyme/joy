from django.contrib import admin
from .models import Member
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class MemberAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('first_name','last_name','email','sex','profile_pic','created_at')

admin.site.register(Member, MemberAdmin)
