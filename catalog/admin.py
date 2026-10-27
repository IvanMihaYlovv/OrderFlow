from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Category, Material, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'is_available', 'created_at')
    list_filter = ('category', 'is_available', 'materials')
    search_fields = ('name', 'description')
    filter_horizontal = ('materials',)
