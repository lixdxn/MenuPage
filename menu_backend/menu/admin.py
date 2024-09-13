from django.contrib import admin
from .models import Menu, MenuItem


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    """
    Для управления меню.
    """
    model = MenuItem
    list_display = ['name']
    search_fields = ['name']

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    """
    Для управления элементами меню.
    """
    list_display = ['title', 'menu', 'parent', 'url_name']
    list_filter = ['menu', 'parent']
    search_fields = ['title', 'url_name']
    ordering = ['menu', 'parent', 'title']
