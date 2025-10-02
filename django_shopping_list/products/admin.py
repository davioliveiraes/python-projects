from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
   list_display = ("name", "price", "quantity", "total_price", "purchased", "created_at")
   list_filter = ("purchased", "created_at")
   search_fields = ("name",)
   list_editable = ("quantity", "purchased")
