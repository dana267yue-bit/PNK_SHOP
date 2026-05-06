from django.urls import path
from . import views

urlpatterns = [
    # --- Public Pages ---
    path('', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('shop/', views.shop, name='shop'),
    path('product/<int:id>/', views.ShopDetails, name='ShopDetails'),
    path('blog/', views.blog_page, name='blog_page'),
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('contact/', views.contact, name='contact'),
    path('About/', views.About, name='About'),

    # --- Authentication ---
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('profile/', views.profile_view, name='profile'),

    # --- Dashboard & Product Management ---
    path('dashboard/', views.dashboard, name='dashboard'),
    path('productList/', views.product_list, name='product_list'),
    path('dashboard/add/', views.add_product, name='add_product'),
    path('dashboard/edit/<int:pk>/', views.edit_product, name='edit_product'),
    path('dashboard/delete/<int:pk>/', views.delete_product, name='delete_product'),
    path('ProductsManagementActions/', views.ProductsManagementActions, name='ProductsManagementActions'),

    # --- User Management ---
    path('manage-users/', views.manage_users, name='manage_users'),
    path('delete-user/<int:user_id>/', views.delete_user, name='delete_user'),

    # --- Slideshow Management ---
    path('manage-slideshow/', views.manage_slideshow, name='manage_slideshow'),
    path('manage-slideshow/add/', views.add_slideshow, name='add_slideshow'),
    path('manage-slideshow/edit/<int:pk>/', views.edit_slideshow, name='edit_slideshow'),
    path('manage-slideshow/delete/<int:pk>/', views.delete_slideshow, name='delete_slideshow'),
    # សម្រាប់ link ចាស់ដែលបងធ្លាប់ប្រើ
    path('slideshow/', views.slideshow_view, name='slideshow_view'),

    # --- Blog Management ---
    path('manage/blog/add/', views.manage_add_blog, name='manage_add_blog'),

    # --- Other Features ---
    path('add-to-cart/<int:id>/', views.add_to_cart, name='add_to_cart'),
]