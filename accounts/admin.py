from django.contrib import admin
from .models import Product, Brand, ProductImage, Blog, Category

# ១. បង្កើត Inline សម្រាប់បង្ហាញរូបភាពតូចៗច្រើនក្នុងទំព័រ Product តែមួយ
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 3

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # ដូរពី 'name' មក 'title'
    list_display = ['title', 'brand', 'price', 'stock'] 
    inlines = [ProductImageInline]

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_added')
    search_fields = ('title',)

admin.site.register(Category)