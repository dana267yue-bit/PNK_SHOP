from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import authenticate, login as auth_login, logout
from .models import Product, Brand, Blog, ProductImage, Slideshow, Category
from django.contrib.auth.forms import UserCreationForm

# --- Permission Check ---
def is_admin(user):
    return user.is_authenticated and (user.is_staff or user.is_superuser)

# --- Customer Side Views ---
def home(request):
    slides = Slideshow.objects.filter(is_active=True)
    products = Product.objects.all().order_by('-created_at')[:8]
    return render(request, 'accounts/shop/home.html', {'slides': slides, 'products': products})

def index(request):
    slides = Slideshow.objects.all().order_by('-id')
    products = Product.objects.all().order_by('-id')[:8]
    brands = Brand.objects.all()
    sections = [('phone', 'Latest Phones'), ('tablet', 'Latest Tablets')]
    return render(request, 'accounts/shop/index.html', {
        'products': products, 'brands': brands, 'sections': sections, 'slides': slides
    })

def shop(request):
    products = Product.objects.all()
    brands = Brand.objects.all()
    return render(request, 'accounts/shop/shop.html', {'products': products, 'brands': brands})

def ShopDetails(request, id):
    product = get_object_or_404(Product, id=id)
    related_products = Product.objects.filter(brand=product.brand).exclude(id=id)[:4]
    return render(request, 'accounts/shop/shop-details.html', {
        'product': product, 'related_products': related_products
    })

def blog_page(request):
    blogs = Blog.objects.all().order_by('-date_added')
    return render(request, 'accounts/shop/blog.html', {'blogs': blogs})

def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    return render(request, 'accounts/shop/blog-details.html', {'blog': blog})

def contact(request):
    return render(request, 'accounts/shop/contact.html')

def About(request):
    return render(request, 'accounts/shop/about.html')

def login_view(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user) 
            
            return redirect('home') 
        else:
            messages.error(request, "ឈ្មោះអ្នកប្រើប្រាស់ ឬលេខសម្ងាត់មិនត្រឹមត្រូវ!")
            
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

# --- មុខងារចុះឈ្មោះ (Register) ---
def register_view(request):
     if request.method == 'POST':
         form = UserCreationForm(request.POST)
         if form.is_valid():
             form.save()
             messages.success(request, "ចុះឈ្មោះជោគជ័យ! សូមចូលប្រើប្រាស់។")
             return redirect('login')
         else:
             # ប្រសិនបើ Form មិនត្រឹមត្រូវ វានឹង Render ត្រឡប់មកវិញជាមួយ errors
          messages.error(request, "ការចុះឈ្មោះមិនជោគជ័យ។ សូមពិនិត្យកំហុសខាងក្រោម!")
     else:
         form = UserCreationForm()
     return render(request, 'accounts/register.html', {'form': form})



@login_required
def profile_view(request):
    user = request.user
    if request.method == 'POST':
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        user.save()
        messages.success(request, 'ប្រវត្តិរូបត្រូវបានកែប្រែជោគជ័យ!')
        return redirect('profile_view')
    return render(request, 'accounts/shop/profile.html', {'user': user})




# --- Admin Dashboard & Product Views ---
@user_passes_test(is_admin)
def dashboard(request):
    context = {
        'total_products': Product.objects.count(),
        'total_brands': Brand.objects.count(),
    }
    return render(request, 'accounts/dashboard/dashboard.html', context)

@user_passes_test(is_admin)
def product_list(request):
    products = Product.objects.all().order_by('-id')
    return render(request, 'accounts/dashboard/product_list.html', {'products': products})

@user_passes_test(is_admin)
def add_product(request):
    return render(request, 'accounts/dashboard/add_product.html')

@user_passes_test(is_admin)
def edit_product(request, pk):
    return render(request, 'accounts/dashboard/add_product.html')

@user_passes_test(is_admin)
def delete_product(request, pk):
    return redirect('product_list')

# --- User Management ---
@user_passes_test(is_admin)
def manage_users(request):
    users = User.objects.all().order_by('-date_joined')
    return render(request, 'accounts/dashboard/manage_users.html', {'users': users})

@user_passes_test(is_admin)
def delete_user(request, user_id):
    return redirect('manage_users')

# --- Slideshow Management ---
@user_passes_test(is_admin)
def manage_slideshow(request):
    slides = Slideshow.objects.all()
    return render(request, 'accounts/dashboard/manage_slideshow.html', {'slides': slides})

@user_passes_test(is_admin)
def slideshow_view(request):
    return render(request, 'accounts/includes/Slideshow.html')

@user_passes_test(is_admin)
def add_slideshow(request):
    return render(request, 'accounts/includes/add_slideshow.html')

@user_passes_test(is_admin)
def edit_slideshow(request, pk):
    return render(request, 'accounts/includes/add_slideshow.html')

@user_passes_test(is_admin)
def delete_slideshow(request, pk):
    return redirect('slideshow_view')

# --- Other Features ---
def add_to_cart(request, id):
    return redirect('home')

@user_passes_test(is_admin)
def manage_add_blog(request):
    return render(request, 'accounts/shop/add_blog.html')

@user_passes_test(is_admin)
def ProductsManagementActions(request):
     """ទំព័រមជ្ឈមណ្ឌលគ្រប់គ្រង (Dashboard Main)"""
     # ទាញយកទិន្នន័យខ្លះៗមកបង្ហាញ (បើសិនចង់បង្ហាញចំនួនសរុបលើ Dashboard)
     products = Product.objects.all()
 
     context = {
         'products': products,
         'title': 'មជ្ឈមណ្ឌលគ្រប់គ្រងទូរស័ព្ទ',
     }
     return render(request, 'accounts/dashboard/Products_Management_Actions.html', context)

from django.contrib.auth.decorators import login_required
