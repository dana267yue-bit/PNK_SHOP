
from django.contrib import admin
#from .models import (
    # Product,
    # ProductImage,
    # Brand,
    # Blog,
    # Category,
    # Order,
    # OrderItem,
 #   UserProfile,  # รក្សាទុកតែ UserProfile ដែលនៅក្នុង accounts
    # ProductReview,
#)

# ============================================================
# ផ្នែកខាងក្រោមនេះត្រូវបានបិទបណ្តោះអាសន្ន ដើម្បីកុំឱ្យ Django គាំង (Crash)
# ============================================================

# # ==========================
# # PRODUCT IMAGE INLINE
# # ==========================
# class ProductImageInline(admin.TabularInline):
#     model = ProductImage
#     extra = 3


# # ==========================
# # PRODUCT ADMIN
# # ==========================
# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = (
#         'name',
#         'category',
#         'brand',
#         'price',
#         'stock',
#         'created_at'
#     )

#     list_filter = (
#         'category',
#         'brand'
#     )

#     search_fields = (
#         'name',
#         'description'
#     )

#     inlines = [ProductImageInline]


# # ==========================
# # BRAND ADMIN
# # ==========================
# @admin.register(Brand)
# class BrandAdmin(admin.ModelAdmin):
#     list_display = ('name',)


# # ==========================
# # CATEGORY ADMIN
# # ==========================
# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = (
#         'name',
#         'slug'
#     )

#     prepopulated_fields = {
#         'slug': ('name',)
#     }


# # ==========================
# # BLOG ADMIN
# # ==========================
# @admin.register(Blog)
# class BlogAdmin(admin.ModelAdmin):
#     list_display = (
#         'name',
#         'date_added'
#     )

#     search_fields = (
#         'name',
#     )


# # ==========================
# # REVIEW ADMIN
# # ==========================
# @admin.register(ProductReview)
# class ProductReviewAdmin(admin.ModelAdmin):
#     list_display = (
#         'product',
#         'name',
#         'rating',
#         'created_at'
#     )


# # ==========================
# # ORDER ITEM INLINE
# # ==========================
# class OrderItemInline(admin.TabularInline):
#     model = OrderItem
#     extra = 0


# # ==========================
# # ORDER ADMIN
# # ==========================
# @admin.register(Order)
# class OrderAdmin(admin.ModelAdmin):
#     list_display = (
#         'id',
#         'user',
#         'first_name',
#         'last_name',
#         'phone',
#         'city',
#         'total_amount',
#         'status',
#         'created_at'
#     )

#     list_filter = (
#         'status',
#         'created_at',
#         'city'
#     )

#     search_fields = (
#         'first_name',
#         'last_name',
#         'phone',
#         'email'
#     )

#     list_editable = (
#         'status',
#     )

#     inlines = [
#         OrderItemInline
#     ]


# ==========================
# USER PROFILE
# ==========================
#admin.site.register(UserProfile)