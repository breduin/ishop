from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from .models import Category, Product

admin.site.register(Product)


admin.site.register(
    Category,
    DraggableMPTTAdmin,
    list_display=(
        'tree_actions',
        'indented_title',
        # ...more fields if you feel like it...
    ),
    list_display_links=(
        'indented_title',
    ),
    prepopulated_fields = {"slug": ("name", )},
)

