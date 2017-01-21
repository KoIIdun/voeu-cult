from django.contrib import admin
from .models import Product, Size, Image
# Register your models here.

class SizeAdmin(admin.TabularInline):
    model = Size
    extra = 1

class ImageAdmin(admin.TabularInline):
    model = Image
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageAdmin, SizeAdmin]
    list_display = ('type', 'manufacturer', 'name', 'cost', 'new', 'sells')
    list_filter = ['type']

admin.site.register(Product, ProductAdmin)