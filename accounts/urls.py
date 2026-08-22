from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    # --- Authentication & User Management ---
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('settings/', views.settings_page, name='settings_page'),
    path('manage-users/', views.manage_users, name='manage_users'),
    path('add-user/', views.add_user, name='add_user'),
    path('user-detail/<int:user_id>/', views.user_detail_api, name='user_detail_api'),
    path('toggle-user-active/<int:user_id>/', views.toggle_user_active, name='toggle_user_active'),
    path('delete-user/<int:user_id>/', views.delete_user, name='delete_user'),
    
    # --- Inventory Management ---
    path('inventory/', views.inventory_page, name='inventory_page'),
    path('update-stock/<int:product_id>/', views.update_stock, name='update_stock'),
    path('export-inventory-csv/', views.export_inventory_csv, name='export_inventory_csv'),
    path('export-orders-csv/', views.export_orders_csv, name='export_orders_csv'),

    # --- Category & Brand Management ---
    path('categories/', views.categories_page, name='categories_page'),
    path('add-category/', views.add_category, name='add_category'),
    path('delete-category/<int:category_id>/', views.delete_category, name='delete_category'),
    path('add-brand/', views.add_brand, name='add_brand'),
    path('delete-brand/<int:brand_id>/', views.delete_brand, name='delete_brand'),

    # --- Admin Blog Management ---
    path('manage-blog/', views.manage_blog, name='manage_blog'),
    path('blog-detail/<int:pk>/', views.dashboard_blog_detail, name='dashboard_blog_detail'),
    path('add-blog/', views.add_blog, name='add_blog'),
    path('edit-blog/<int:pk>/', views.edit_blog, name='edit_blog'),
    path('delete-blog/<int:pk>/', views.delete_blog, name='delete_blog'),

    # --- Admin Slideshow Management ---
    path('manage-slideshow/', views.manage_slideshow, name='manage_slideshow'),
    path('add-slideshow/', views.add_slideshow, name='add_slideshow'),
    path('edit-slideshow/<int:pk>/', views.edit_slideshow, name='edit_slideshow'),
    path('delete-slideshow/<int:pk>/', views.delete_slideshow, name='delete_slideshow'),

    # --- Dashboard & Order Management ---
    path('dashboard/', views.dashboard, name='dashboard'),
    path('messages/', views.customer_messages, name='customer_messages'),
    path('api/send-chat-message/', views.send_chat_message_api, name='send_chat_message_api'),
    path('api/update-auto-reply-settings/', views.update_auto_reply_settings_api, name='update_auto_reply_settings_api'),
    path('api/customer-send-chat/', views.customer_send_chat_api, name='customer_send_chat_api'),
    path('api/get-customer-chat-history/', views.get_customer_chat_history_api, name='get_customer_chat_history_api'),
    path('api/get-latest-messages/', views.get_latest_messages_api, name='get_latest_messages_api'),
    path('api/admin-heartbeat/', views.admin_heartbeat_api, name='admin_heartbeat_api'),
    path('api/get-notifications/', views.get_notifications_api, name='get_notifications_api'),
    path('api/mark-notifications-read/', views.mark_notifications_read_api, name='mark_notifications_read_api'),
    path('upload/', views.upload_page, name='upload_page'),
    path('reports/', views.report_page, name='report_page'),
    path('orders/', views.order_list, name='order_list'),
    path('confirm-order/<int:order_id>/', views.confirm_order, name='confirm_order'),
    path('update-order-status/<int:order_id>/', views.update_order_status, name='update_order_status'),
    path('order-detail/<int:order_id>/', views.order_detail_api, name='order_detail_api'),
    path('export-orders-csv/', views.export_orders_csv, name='export_orders_csv'),
    path('export-orders-pdf/', views.export_orders_pdf, name='export_orders_pdf'),
    path('export-top-products-csv/', views.export_top_products_csv, name='export_top_products_csv'),
    path('export-top-products-pdf/', views.export_top_products_pdf, name='export_top_products_pdf'),
    path('export-vip-customers-csv/', views.export_vip_customers_csv, name='export_vip_customers_csv'),
    path('export-vip-customers-pdf/', views.export_vip_customers_pdf, name='export_vip_customers_pdf'),
    path('export-low-stock-csv/', views.export_low_stock_csv, name='export_low_stock_csv'),
    path('export-low-stock-pdf/', views.export_low_stock_pdf, name='export_low_stock_pdf'),
]