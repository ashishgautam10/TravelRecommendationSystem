from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import location
@admin.register(location)
class ViewAdmin(ImportExportModelAdmin):
    pass
