from django.contrib import admin


from .models import Categories, Products, Orders


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'user', 'price',)
    search_fields = ['category__name']


class OrdersAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'product_name', 'category', 'price')


admin.site.register(Categories)
admin.site.register(Products, ProductsAdmin)
admin.site.register(Orders, OrdersAdmin)
