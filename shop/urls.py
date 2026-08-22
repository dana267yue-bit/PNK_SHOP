# shop/urls.py
from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    # --- Customer Side - Shop & Pages ---
    # កែសម្រួល៖ ប្តូរពី 'shop/' ទៅជា '' (ទទេ) 🚀
    path('', views.shop, name='shop'), 
    
    path('product/<int:id>/', views.ShopDetails, name='product_details'),
    path('product/<int:product_id>/add-review/', views.add_review, name='add_review'),

    # --- Customer Side - Blog ---
    path('blog/', views.blog_page, name='blog_page'),
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),

    # --- Shopping Cart & Checkout ---
    path('cart/', views.cart_view, name='cart_view'),
    path('add-to-cart/<int:id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/update/<int:product_id>/', views.update_cart, name='update_cart'),
    path('remove-from-cart/<int:id>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.checkout_view, name='checkout'),

    # --- Admin Product Management ---
    path('productList/', views.product_list, name='product_list'),
    path('dashboard/add/', views.add_product, name='add_product'),
    path('dashboard/edit/<int:pk>/', views.edit_product, name='edit_product'),
    path('dashboard/delete/<int:pk>/', views.delete_product, name='delete_product'),
    path('dashboard/delete-gallery-image/<int:pk>/', views.delete_gallery_image, name='delete_gallery_image'),
    path('order-waiting/<int:order_id>/', views.order_waiting_view, name='order_waiting'),
    path('confirm-order/<int:order_id>/', views.confirm_order, name='confirm_order'),
    path('order/success/<int:order_id>/', views.order_success_view, name='order_success'),
    path('order/check-status/<int:order_id>/', views.check_order_status, name='check_order_status'),
    path('order/latest/', views.latest_order_shortcut, name='latest_order_shortcut'),
    path('order/history/', views.order_history_view, name='order_history'),
    path('subscribe-newsletter/', views.subscribe_newsletter, name='subscribe_newsletter'),
]