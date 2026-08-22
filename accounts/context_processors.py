from decimal import Decimal
from shop.models import Product, Order

def cart_context(request):
    cart = request.session.get('cart', {})
    total_items = 0
    total_price = Decimal('0.00')
    
    for product_id, item_data in cart.items():
        try:
            product = Product.objects.get(id=product_id)
            quantity = item_data.get('quantity', 1)
            total_items += quantity
            total_price += product.price * quantity 
        except Product.DoesNotExist:
            continue
            
    return {
        'global_cart_total_items': total_items,
        'global_cart_total_price': total_price,
    }

def dashboard_notifications(request):
    if request.user.is_authenticated and (request.user.is_staff or request.user.is_superuser):
        from accounts.models import ChatMessage
        from django.contrib.auth.models import User
        from django.utils import timezone
        from datetime import timedelta
        
        # 1. Pending Orders (with customer profile)
        pending_orders_qs = Order.objects.filter(status='Pending').select_related('user', 'user__profile').order_by('-id')
        pending_orders_count = pending_orders_qs.count()
        recent_pending_orders = list(pending_orders_qs[:5])
        
        # 2. Low / Out of stock (stock <= 5)
        low_stock_qs = Product.objects.filter(stock__lte=5).order_by('stock')
        low_stock_count = low_stock_qs.count()
        recent_low_stocks = list(low_stock_qs[:5])
        
        # 3. New registered customers (with profile)
        recent_customers_qs = User.objects.filter(is_staff=False, is_superuser=False).select_related('profile').order_by('-id')
        last_seen_cust_id = request.session.get('last_seen_customer_id')
        if last_seen_cust_id is not None:
            unread_cust_qs = recent_customers_qs.filter(id__gt=last_seen_cust_id)
            new_customers_count = unread_cust_qs.count()
            recent_customers = list(unread_cust_qs[:5])
        else:
            unread_cust_qs = recent_customers_qs.filter(date_joined__gte=timezone.now() - timedelta(days=7))
            new_customers_count = unread_cust_qs.count()
            recent_customers = list(unread_cust_qs[:5])
        
        # 4. Unread chat messages
        unread_chat_count = ChatMessage.objects.filter(sender='customer', is_read=False).count()
        
        # Total notifications count
        total_notifications_count = pending_orders_count + low_stock_count + new_customers_count + unread_chat_count
        
        return {
            'pending_orders_count': pending_orders_count,
            'recent_pending_orders': recent_pending_orders,
            'low_stock_count': low_stock_count,
            'recent_low_stocks': recent_low_stocks,
            'new_customers_count': new_customers_count,
            'recent_customers': recent_customers,
            'unread_chat_count': unread_chat_count,
            'total_notifications_count': total_notifications_count,
        }
    return {
        'pending_orders_count': 0,
        'recent_pending_orders': [],
        'low_stock_count': 0,
        'recent_low_stocks': [],
        'new_customers_count': 0,
        'recent_customers': [],
        'unread_chat_count': 0,
        'total_notifications_count': 0,
    }

def store_settings_context(request):
    try:
        from accounts.models import StoreSetting
        store_settings = StoreSetting.get_settings()
    except Exception:
        store_settings = None

    user_latest_order = None
    if request.user.is_authenticated:
        try:
            user_latest_order = Order.objects.filter(user=request.user).order_by('-id').first()
        except Exception:
            pass

    return {
        'store_settings': store_settings,
        'user_latest_order': user_latest_order,
    }