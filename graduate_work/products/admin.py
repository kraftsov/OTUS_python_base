from django.contrib import admin

from products.models import Product, ProductCategory, Basket

# admin.site.register(ProductCategory)
# admin.site.register(Product)
admin.site.register(Basket)


@admin.register(ProductCategory)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    list_filter = ['name']
    fields = ('name',
              'slug',
              'image',
              'description',
              )
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'price', 'quantity', 'category', 'available')
    list_filter = ['available', 'created', 'updated']
    fields = ('name',
              'slug',
              'image',
              'description',
              'short_description',
              ('price', 'quantity', 'available'),
              'category',
              'created',
              )
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ('created',)
    ordering = ('name',)
    search_fields = ('name',)


class BasketAdminInline(admin.TabularInline):
    model = Basket
    fields = ('product',
              'quantity',
              'created_timestamp'
              )
    readonly_fields = ('product',
                       'created_timestamp',
                       )
    extra = 0
