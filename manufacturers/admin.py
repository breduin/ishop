from django.contrib import admin
from .models import Manufacturer


class ManufacturerAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name", )}

admin.site.register(Manufacturer, ManufacturerAdmin)