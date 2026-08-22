from django.shortcuts import render, get_object_or_404
from shop.models import Product, Brand, Category, Blog
from accounts.models import Slideshow

def home(request):
    # ១. ទាញយកផលិតផលទូរស័ព្ទថ្មីៗសម្រាប់ New Arrivals (Smartphones only)
    new_products = Product.objects.filter(category__slug__in=['smart-phone', 'smartphone', 'smartphones']).order_by('-created_at')[:8]
    if not new_products.exists():
        new_products = Product.objects.filter(category__name__icontains='phone').order_by('-created_at')[:8]
    
    # ២. ទាញយកផលិតផលទូរស័ព្ទបញ្ចុះតម្លៃសម្រាប់ Hot Discount (Smartphones only)
    promotional_products = Product.objects.filter(category__slug__in=['smart-phone', 'smartphone', 'smartphones'], old_price__gt=0).order_by('-created_at')[:8]
    if not promotional_products.exists():
        promotional_products = Product.objects.filter(category__name__icontains='phone', old_price__gt=0).order_by('-created_at')[:8]
    
    # ៣. ទាញយកគ្រឿងបន្លាស់ស្មាតហ្វូន (Accessories)
    accessory_products = Product.objects.filter(category__slug__in=['accessories', 'accessory']).order_by('-created_at')[:8]
    if not accessory_products.exists():
        accessory_products = Product.objects.filter(category__name__icontains='accessor').order_by('-created_at')[:8]

    # ៤. ទាញយកទិន្នន័យស្លាយ
    slides_data = Slideshow.objects.all()
    
    # ៥. ទាញយកប្រភេទទំនិញ (Categories), ម៉ាកយីហោ (Brands) នឹងព័ត៌មាន (Blogs)
    categories = Category.objects.all()
    brands = Brand.objects.all()
    blogs = Blog.objects.all().order_by('-created_at')[:3]
    
    context = {
        'new_products': new_products,
        'promotional_products': promotional_products,
        'accessory_products': accessory_products,
        'slides': slides_data,  
        'categories': categories,
        'brands': brands,
        'blogs': blogs,
    }
    return render(request, 'core/home.html', context)

def contact(request):
    return render(request, 'core/contact.html')

def about(request):
    brands = Brand.objects.all()
    return render(request, 'core/about.html', {'brands': brands})
    
def product_details(request, id):
    product = get_object_or_404(Product, id=id)
    # Related products should match both brand and category
    related_products = Product.objects.filter(brand=product.brand, category=product.category).exclude(id=id)[:4]
    return render(request, 'accounts/shop/shop-details.html', {'product': product, 'related_products': related_products})