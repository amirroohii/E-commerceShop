from django.contrib import admin
from .models import Product,ProductCategory,ProductGallery
# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_filter = ('category', 'is_active')
    list_display = ('title','price', 'is_active', 'is_deleted')
    list_editable = ('price', 'is_active', 'is_deleted')

admin.site.register(ProductCategory)
admin.site.register(ProductGallery)