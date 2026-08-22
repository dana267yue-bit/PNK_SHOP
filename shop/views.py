from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
from django.db.models import F, Q, Avg, Sum
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from .models import Product, Brand, Category, ProductImage, Order, OrderItem, Blog, ProductReview, Subscriber

from accounts.models import Slideshow
from .form import ProductForm
from .cart import Cart
from django.db import transaction

def is_admin(user):
    return user.is_authenticated and (user.is_staff or user.is_superuser)

# --- Customer Side Views ---
def home(request):
    slides = Slideshow.objects.filter(is_active=True)
    products = Product.objects.all().order_by('-created_at')[:8]
    new_products = Product.objects.order_by('-id')[:4] 
    promotional_products = Product.objects.filter(old_price__gt=F('price'))[:4]
    
    context = {
        'slides': slides, 'products': products,
        'new_products': new_products, 'promotional_products': promotional_products,
    }
    return render(request, 'core/home.html', context)

def index(request):
    slides = Slideshow.objects.all().order_by('-id')
    products = Product.objects.all().order_by('-id')[:8]
    brands = Brand.objects.all()
    sections = [('phone', 'Latest Phones'), ('tablet', 'Latest Tablets')]
    return render(request, 'accounts/shop/index.html', {
        'products': products, 'brands': brands, 'sections': sections, 'slides': slides
    })

def shop(request):
    # 1. យកទិន្នន័យដើមទាំងអស់
    products = Product.objects.all()
    categories = Category.objects.all()
    brands = Brand.objects.all()

    # 2. ទទួលយកប៉ារ៉ាម៉ែត្រពី URL (GET Request)
    category_id = request.GET.get('category')
    brand_id = request.GET.get('brand')
    search_query = request.GET.get('search')
    sort_option = request.GET.get('sort', 'newest')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    # 3. ធ្វើការ Filter ទិន្នន័យតាមលក្ខខណ្ឌ
    if category_id:
        products = products.filter(category_id=category_id)
    if brand_id:
        products = products.filter(brand_id=brand_id)
    if search_query:
        products = products.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(brand__name__icontains=search_query) |
            Q(category__name__icontains=search_query)
        )
    if min_price and min_price.isdigit():
        products = products.filter(price__gte=int(min_price))
    if max_price and max_price.isdigit():
        products = products.filter(price__lte=int(max_price))

    # 4. ធ្វើការ Order / Sort ទិន្នន័យ
    if sort_option == 'price_asc':
        products = products.order_by('price')
    elif sort_option == 'price_desc':
        products = products.order_by('-price')
    elif sort_option == 'name_asc':
        products = products.order_by('name')
    else:
        products = products.order_by('-id')

    # 5. ធ្វើការបែងចែកទំព័រ (Pagination)
    paginator = Paginator(products, 9)  # បង្ហាញ 9 ផលិតផលក្នុងមួយទំព័រ
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # 6. រៀបចំ Context ដើម្បីផ្ញើទៅ Template
    context = {
        'products': page_obj, 
        'categories': categories, 
        'brands': brands,
        'selected_category': category_id, 
        'selected_brand': brand_id, 
        'selected_sort': sort_option,
        'search_query': search_query,
        'min_price': min_price,
        'max_price': max_price,
    }

    # 7. ត្រួតពិនិត្យថា តើនេះជាការហៅពី HTMX ឬការ Load ទំព័រធម្មតា?
    if request.headers.get('HX-Request'):
        # ផ្ញើតែផ្នែក partial សម្រាប់ Update ក្នុងទំព័រហាង
        return render(request, 'accounts/shop/product_list_partial.html', context)
        
    # ផ្ញើទំព័រហាងទាំងមូល
    return render(request, 'accounts/shop/shop.html', context)

def ShopDetails(request, id):
    product = get_object_or_404(Product, id=id)
    related_products = Product.objects.filter(brand=product.brand).exclude(id=id)[:4]
    reviews = product.reviews.all()
    avg_rating = reviews.aggregate(Avg('rating'))['rating__avg'] if reviews.exists() else 4.9
    return render(request, 'accounts/shop/shop-details.html', {
        'product': product,
        'related_products': related_products,
        'reviews': reviews,
        'avg_rating': round(float(avg_rating), 1),
        'reviews_count': reviews.count() if reviews.exists() else 12,
    })

def add_review(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        rating = int(request.POST.get('rating', 5))
        comment = request.POST.get('comment', '').strip()
        user = request.user if request.user.is_authenticated else None
        
        if comment:
            if not user:
                from django.contrib.auth.models import User
                user = User.objects.first()
            ProductReview.objects.create(
                product=product,
                user=user,
                rating=rating,
                comment=comment
            )
            messages.success(request, 'អរគុណសម្រាប់ការសរសេរ Review របស់អ្នក!')
        else:
            messages.error(request, 'សូមបញ្ចូលមតិយោបល់របស់អ្នក!')
    return redirect('shop:product_details', id=product_id)

def blog_page(request):
    search_query = request.GET.get('search', '').strip()
    blogs = Blog.objects.all().order_by('-created_at')
    if search_query:
        blogs = blogs.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(slug__icontains=search_query)
        )
    return render(request, 'accounts/shop/blog.html', {
        'blogs': blogs,
        'search_query': search_query,
    })

def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    recent_blogs = Blog.objects.exclude(pk=blog.pk).order_by('-created_at')[:4]
    return render(request, 'accounts/shop/blog-details.html', {
        'blog': blog,
        'recent_blogs': recent_blogs
    })

def contact(request):
    return render(request, 'core/contact.html')

def About(request):
    return render(request, 'accounts/shop/about.html')


# --- Admin Product Management ---
@user_passes_test(is_admin)
def product_list(request):
    from django.db.models import Q
    
    product_qs = Product.objects.all().select_related('brand').order_by('-id')
    
    total_count = product_qs.count()
    in_stock_count = product_qs.filter(stock__gt=0).count()
    out_of_stock_count = product_qs.filter(stock=0).count()
    brands_count = Brand.objects.count()
    all_brands = Brand.objects.all().order_by('name')

    # Category filter
    all_categories = Category.objects.all().order_by('name')
    category_filter = request.GET.get('category', 'all')
    if category_filter != 'all' and category_filter.isdigit():
        product_qs = product_qs.filter(category_id=int(category_filter))

    brand_filter = request.GET.get('brand', 'all')
    if brand_filter != 'all' and brand_filter.isdigit():
        product_qs = product_qs.filter(brand_id=int(brand_filter))
        
    stock_filter = request.GET.get('stock', 'all')
    if stock_filter == 'in_stock':
        product_qs = product_qs.filter(stock__gt=0)
    elif stock_filter == 'out_of_stock':
        product_qs = product_qs.filter(stock=0)

    search_query = request.GET.get('search', '').strip()
    if search_query:
        product_qs = product_qs.filter(
            Q(name__icontains=search_query) | Q(brand__name__icontains=search_query)
        )

    paginator = Paginator(product_qs, 15)
    page_number = request.GET.get('page', 1)
    products = paginator.get_page(page_number)
    
    context = {
        'products': products,
        'page_obj': products,
        'total_count': total_count,
        'in_stock_count': in_stock_count,
        'out_of_stock_count': out_of_stock_count,
        'brands_count': brands_count,
        'all_brands': all_brands,
        'all_categories': all_categories,
        'brand_filter': brand_filter,
        'stock_filter': stock_filter,
        'category_filter': category_filter,
        'search_query': search_query,
    }
    return render(request, 'accounts/dashboard/product_list.html', context)

@user_passes_test(is_admin)
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            gallery_files = []
            for field in ['gallery_image_1', 'gallery_image_2', 'gallery_image_3']:
                if field in request.FILES:
                    gallery_files.append(request.FILES[field])
            gallery_files.extend(request.FILES.getlist('gallery_images'))

            for img in gallery_files[:3]:
                if img:
                    ProductImage.objects.create(product=product, image=img)
            return JsonResponse({'success': True})
        html_form = render_to_string('accounts/includes/add_product_form.html', {'form': form}, request=request)
        return JsonResponse({'success': False, 'html_form': html_form})
    form = ProductForm()
    return render(request, 'accounts/includes/add_product_form.html', {'form': form})

@user_passes_test(is_admin)
def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            product = form.save()
            gallery_files = []
            for field in ['gallery_image_1', 'gallery_image_2', 'gallery_image_3']:
                if field in request.FILES:
                    gallery_files.append(request.FILES[field])
            gallery_files.extend(request.FILES.getlist('gallery_images'))

            for img in gallery_files[:3]:
                if img:
                    ProductImage.objects.create(product=product, image=img)
            return JsonResponse({'success': True})
        html_form = render_to_string('accounts/includes/edit_product_form.html', {'form': form, 'product': product}, request=request)
        return JsonResponse({'success': False, 'html_form': html_form})
    form = ProductForm(instance=product)
    return render(request, 'accounts/includes/edit_product_form.html', {'form': form, 'product': product})

@user_passes_test(is_admin)
def delete_gallery_image(request, pk):
    g_img = get_object_or_404(ProductImage, pk=pk)
    if request.method == 'POST':
        g_img.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False, 'error': 'Method not allowed'})

@user_passes_test(is_admin)
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False, 'error': 'Method not allowed'})

@user_passes_test(is_admin)
def ProductsManagementActions(request):
    products = Product.objects.all()
    return render(request, 'accounts/dashboard/products.html', {'products': products, 'title': 'មជ្ឈមណ្ឌលគ្រប់គ្រងទូរស័ព្ទ'})


# --- Shopping Cart & Checkout Features (Refactored using Class Cart) ---
def cart_view(request):
    cart = Cart(request)
    cart_items = []
    to_remove = []
    
    # ប្រើ .items() របស់ dictionary ដើម្បីទទួលបានទាំង key (product_id) និង value (data)
    for product_id, item in list(cart.cart.items()): 
        try:
            product = Product.objects.get(id=product_id)
            cart_items.append({
                'product': product,
                'quantity': item['quantity'],
                'id': product_id, # ប្រើ product_id ដែលយើងបានមកពី loop
                'total_price': float(item['price']) * item['quantity']
            })
        except ObjectDoesNotExist:
            to_remove.append(product_id)

    # ជូតសម្អាត ID ទំនិញដែលត្រូវបានលុបចេញពី Database រួចហើយ
    if to_remove:
        for pid in to_remove:
            if pid in cart.cart:
                del cart.cart[pid]
        cart.save()
    
    total_items = sum(item['quantity'] for item in cart_items)

    return render(request, 'accounts/shop/shoping-cart.html', {
        'cart_items': cart_items,
        'total_price': cart.total(),
        'total_items': total_items,
    })
def add_to_cart(request, id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=id)
    quantity = int(request.POST.get('quantity', 1))
    
    # 🎯 ពិនិត្យស្តុកទំនិញ (Inventory Stock Validation)
    if product.stock <= 0:
        messages.error(request, f"ទំនិញ «{product.name}» អស់ពីស្តុកហើយ (Out of Stock)!")
        return redirect(request.META.get('HTTP_REFERER', 'shop:shop'))
    
    current_cart_qty = 0
    pid_str = str(id)
    if pid_str in cart.cart:
        current_cart_qty = cart.cart[pid_str].get('quantity', 0)
        
    total_qty = current_cart_qty + quantity
    if total_qty > product.stock:
        messages.warning(request, f"ទំនិញ «{product.name}» មានស្តុកសល់ត្រឹមតែ {product.stock} ប៉ុណ្ណោះ!")
        return redirect(request.META.get('HTTP_REFERER', 'shop:cart_view'))

    cart.add(product=product, quantity=quantity)
    messages.success(request, f"បានបន្ថែម «{product.name}» ទៅក្នុងកន្ត្រកជោគជ័យ!") 
    return redirect('shop:cart_view')

def update_cart(request, product_id): # កែពី id មកជា product_id ឱ្យដូចក្នុង urls.py
    if request.method == 'POST':
        cart = Cart(request)
        product = Product.objects.filter(id=product_id).first()
        quantity = int(request.POST.get('quantity', 1))
        
        if product:
            if quantity > product.stock:
                messages.warning(request, f"ទំនិញ «{product.name}» មានស្តុកសល់ត្រឹមតែ {product.stock} ប៉ុណ្ណោះ!")
                return redirect('shop:cart_view')

            if quantity > 0:
                cart.remove(product)
                cart.add(product=product, quantity=quantity)
                messages.success(request, "បានធ្វើបច្ចុប្បន្នភាពចំនួនទំនិញ!")
            else:
                cart.remove(product)
                messages.warning(request, "បានលុបទំនិញចេញពីកន្ត្រក!")
        else:
            # បើទំនិញលុបចេញពី DB ហើយ ត្រូវសម្អាតចេញពី Cart Session
            pid_str = str(product_id)
            if pid_str in cart.cart:
                del cart.cart[pid_str]
                cart.save()
            messages.warning(request, "ទំនិញនេះពុំមានក្នុងប្រព័ន្ធទៀតទេ!")
            
    return redirect('shop:cart_view')

def remove_from_cart(request, id):
    cart = Cart(request)
    pid_str = str(id)
    if pid_str in cart.cart:
        del cart.cart[pid_str]
        cart.save()
    messages.warning(request, "បានលុបទំនិញចេញពីកន្ត្រក!")
    return redirect('shop:cart_view')

@login_required
@transaction.atomic  # 🎯 បន្ថែមដើម្បីការពារបើការ Save items ណាមួយបរាជ័យ វានឹង Rollback មិនបង្កើត Order ឡើយ
def checkout_view(request):
    cart = Cart(request) 
    
    # ការពារមិនឱ្យចូលទំព័រ Checkout បើកន្ត្រកទទេ
    if not cart or (hasattr(cart, 'items') and not list(cart.items())):
        messages.warning(request, "កន្ត្រកទំនិញរបស់បងទទេ!")
        return redirect('shop:shop')

    global_cart_total_price = cart.total()

    if request.method == 'POST':
        # 🎯 ១. ចាប់យកទិន្នន័យពី Form
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        city = request.POST.get('city')
        address_1 = request.POST.get('address_1')
        address_2 = request.POST.get('address_2')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        order_notes = request.POST.get('order_notes')
        payment_method = request.POST.get('payment_method')
        
        payment_receipt = request.FILES.get('payment_receipt')

        # 🎯 ២. បង្កើត Order
        order = Order.objects.create(
            user=request.user,
            first_name=first_name,
            last_name=last_name,
            city=city,
            address_1=address_1,
            address_2=address_2,
            phone=phone,
            email=email,
            order_notes=order_notes,
            payment_method=payment_method,
            payment_receipt=payment_receipt if payment_method in ('online', 'khqr') else None,
            total_amount=global_cart_total_price, 
            status='Pending'
        )

        # 🎯 ៣. បញ្ចូលទំនិញទៅក្នុង OrderItem និងកាត់ស្តុកទំនិញ
        order_items_list = [] 
        
        for item in cart.items(): 
            product_id = item.get('id') if isinstance(item, dict) else getattr(item, 'id', None)
            if not product_id: 
                continue 
            
            try:
                product_obj = Product.objects.get(id=product_id)
                qty = item['quantity']
                
                # 🎯 ពិនិត្យ និងកាត់ស្តុកទំនិញស្វ័យប្រវត្តិ
                if product_obj.stock >= qty:
                    product_obj.stock -= qty
                    product_obj.save()
                else:
                    messages.error(request, f"ទំនិញ «{product_obj.name}» មានស្តុកសល់ត្រឹមតែ {product_obj.stock} ប៉ុណ្ណោះ! សូមកែប្រែចំនួនកន្ត្រក។")
                    transaction.set_rollback(True)
                    return redirect('shop:cart_view')

                order_item = OrderItem.objects.create(
                    order=order,
                    product=product_obj,
                    quantity=qty,
                    price=item['price']
                )
                order_items_list.append(order_item)
            except ObjectDoesNotExist:
                continue

        # 🎯 ៤. ផ្ញើដំណឹងទៅ Telegram
        try:
            from .telegram_utils import send_order_to_telegram
            send_order_to_telegram(order, order_items_list)
        except Exception as e:
            # បោះ Error ចូលក្នុង Console Log ដើម្បីកុំឱ្យទំព័រគាំង
            print(f"Telegram Notification Error: {e}")

        # 🎯 ៥. សម្អាតកន្ត្រកទំនិញ រួចរុញទៅកាន់ទំព័ររង់ចាំ (order_waiting)
        cart.clear()
        return redirect('shop:order_waiting', order_id=order.id) 

    # 🔄 ករណី GET: បង្ហាញទំព័រ Checkout ធម្មតា
    last_order = Order.objects.filter(user=request.user).order_by('-id').first()
    context = {
        'cart': cart,
        'global_cart_total_price': global_cart_total_price,
        'last_order': last_order, 
    }
    return render(request, 'accounts/shop/checkout.html', context)

def order_waiting_view(request, order_id):
    """ បង្ហាញទំព័ររង់ចាំ (order_waiting.html) និងប្រើ HTMX Polling ទៅឆែក status """
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'accounts/shop/order_waiting.html', {'order': order})


def check_order_status(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    status_lower = str(order.status).lower()

    if status_lower in ["completed", "confirmed", "processing"]:
        return HttpResponse(f"<script>window.location.href='/shop/order/success/{order_id}/';</script>")
    elif status_lower == "rejected":
        admin_reason = order.admin_note or "សូមទាក់ទងមកកាន់ហាង"
        return HttpResponse(f"""
            <div id="status-badge-container" style="display: inline-block;">
                <span class="badge bg-danger text-white px-3 py-1.5 rounded-pill shadow-sm" style="font-size: 13px;">
                    <i class="bi bi-x-circle-fill me-1"></i> ត្រូវបានបដិសេធ ({admin_reason})
                </span>
            </div>
            <script>
                if (typeof Swal !== 'undefined') {{
                    Swal.fire({{
                        icon: 'error',
                        title: 'ការបញ្ជាទិញត្រូវបានបដិសេធ',
                        text: '{admin_reason}',
                        confirmButtonColor: '#dc3545'
                    }});
                }}
            </script>
        """)

    return HttpResponse("""
        <div id="status-badge-container" style="display: inline-block;">
            <span class="badge bg-warning text-dark px-3 py-1.5 rounded-pill shadow-sm fw-semibold" style="font-size: 13px;">
                <i class="bi bi-hourglass-split me-1"></i> កំពុងរង់ចាំ Admin ពិនិត្យ...
            </span>
        </div>
    """)



def order_success_view(request, order_id):
    """ 📄 បង្ហាញទំព័រជោគជ័យចុងក្រោយ (order_success.html) ជូនអតិថិជន """
    order = get_object_or_404(Order, id=order_id)
    return render(request, "accounts/shop/order_success.html", {"order": order})


@user_passes_test(is_admin)
def confirm_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    order.status = "Confirmed"
    order.save()

    return render(
        request,
        "accounts/dashboard/order_row.html",
        {
            "order": order
        }
    )


@login_required
def latest_order_shortcut(request):
    """ មុខងារស្វែងរក Order ចុងក្រោយបង្អស់របស់ User រួចរុញទៅទំព័រ Success ឬ Waiting """
    # ស្វែងរក Order ចុងក្រោយគេបង្អស់ដែលជារបស់គាត់
    latest_order = Order.objects.filter(user=request.user).order_by('-id').first()
    
    if latest_order:
        # ប្រសិនបើការបញ្ជាទិញកំពុងរង់ចាំការផ្ទៀងផ្ទាត់ (Pending)
        if latest_order.status == 'Pending':
            return redirect('shop:order_waiting', order_id=latest_order.id)
        # ប្រសិនបើបានផ្ទៀងផ្ទាត់រួចរាល់ (Completed / Processing / Rejected)
        return redirect('shop:order_success', order_id=latest_order.id)
    else:
        # បើគាត់មិនទាន់ដែលទិញអ្វីសោះ ឱ្យរុញទៅទំព័រហាង (Shop) វិញ រួចបង្ហាញសារ
        messages.info(request, "បងមិនទាន់មានប្រវត្តិបញ្ជាទិញនៅឡើយទេ!")
        return redirect('shop:shop')

@login_required
def order_history_view(request):
    """ ទំព័របង្ហាញប្រវត្តិការបញ្ជាទិញទាំងអស់របស់ Customer """
    status_filter = request.GET.get('status', 'all').strip()

    orders_qs = Order.objects.filter(user=request.user).prefetch_related('items__product').order_by('-created_at')

    # Summary Statistics
    total_orders_count = orders_qs.count()
    completed_orders_count = orders_qs.filter(status__iexact='Completed').count()
    pending_orders_count = orders_qs.filter(status__iexact='Pending').count()
    processing_orders_count = orders_qs.filter(status__iexact='Processing').count()
    rejected_orders_count = orders_qs.filter(status__iexact='Rejected').count()
    total_spent = orders_qs.filter(status__iexact='Completed').aggregate(total=Sum('total_amount'))['total'] or 0

    # Apply Filter
    if status_filter != 'all':
        orders = orders_qs.filter(status__iexact=status_filter)
    else:
        orders = orders_qs

    context = {
        'orders': orders,
        'status_filter': status_filter,
        'total_orders_count': total_orders_count,
        'completed_orders_count': completed_orders_count,
        'pending_orders_count': pending_orders_count,
        'processing_orders_count': processing_orders_count,
        'rejected_orders_count': rejected_orders_count,
        'total_spent': total_spent,
    }
    return render(request, 'accounts/shop/order_history.html', context)


def subscribe_newsletter(request):
    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        if email:
            subscriber, created = Subscriber.objects.get_or_create(email=email)
            if created:
                messages.success(request, "អរគុណសម្រាប់ការចុះឈ្មោះ! លោកអ្នកនឹងទទួលបានព័ត៌មានថ្មីៗពី PNK SHOP។")
            else:
                messages.info(request, "អ៊ីមែលនេះបានចុះឈ្មោះក្នុងប្រព័ន្ធរួចហើយ។")
        else:
            messages.error(request, "សូមបញ្ចូលអាសយដ្ឋានអ៊ីមែលត្រឹមត្រូវ។")
    return redirect(request.META.get('HTTP_REFERER', 'core:home'))