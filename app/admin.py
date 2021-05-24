from django.contrib import admin

# Register your models here.
from app.models import Product, Store


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass
