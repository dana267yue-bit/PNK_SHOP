from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.conf import settings

# 1. ដាក់ Model ដែលមិនមាន ForeignKey នៅខាងលើគេ
class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='categories/', null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True)
    objects = models.Manager()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = str(slugify(self.name))
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return str(self.name)

class Brand(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='brands/', null=True, blank=True)
    objects = models.Manager()

    def __str__(self) -> str:
        return str(self.name)

# 2. បន្ទាប់មកដាក់ Product
class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True)
    promotion = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    old_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    stock = models.IntegerField(default=0)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    payment_receipt = models.ImageField(upload_to='receipts/', null=True, blank=True)
    status = models.CharField(max_length=20, default='Pending')
    objects = models.Manager()

    def __str__(self) -> str:
        return str(self.name)

# 3. ដាក់ Order និង OrderItem
class Order(models.Model):
    PAYMENT_CHOICES = [('cod', 'COD'), ('khqr', 'KHQR'), ('online', 'KHQR')]
    STATUS_CHOICES = [('Pending', 'Pending'), ('Processing', 'Processing'), ('Completed', 'Completed'), ('Rejected', 'Rejected'),]
    
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    
    # 📌 បន្ថែម Fields ទាំងនេះចូលទៅ
    city = models.CharField(max_length=100)
    address_1 = models.CharField(max_length=255)
    address_2 = models.CharField(max_length=255, null=True, blank=True)
    
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    
    order_notes = models.TextField(null=True, blank=True)
    payment_receipt = models.ImageField(upload_to='receipts/', null=True, blank=True)
    # 📌 បន្ថែម Field នេះចូល ដើម្បីទុកឱ្យ Admin សរសេរប្រាប់មូលហេតុពេល Reject Order
    admin_note = models.TextField(null=True, blank=True, verbose_name="មូលហេតុបដិសេធ")
    objects = models.Manager()

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE) # ពេលនេះ Product បានស្គាល់រួចហើយ
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    objects = models.Manager()

# 4. ដាក់ Model បន្ទាប់បន្សំ
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products/gallery/')
    objects = models.Manager()

class ProductReview(models.Model):
    RATING_CHOICES = ((1, '★☆☆☆☆'), (2, '★★☆☆☆'), (3, '★★★☆☆'), (4, '★★★★☆'), (5, '★★★★★'))
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='product_reviews')
    rating = models.IntegerField(choices=RATING_CHOICES, default=5)
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    class Meta:
        ordering = ['-created_at']

class Blog(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='blogs/')
    created_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    @property
    def title(self):
        return self.name

    @property
    def date_added(self):
        return self.created_at

    def save(self, *args, **kwargs):
        if not self.slug:
            from django.utils.text import slugify
            import time
            base_slug = slugify(self.name)
            if not base_slug:
                base_slug = f"blog-{int(time.time())}"
            unique_slug = base_slug
            counter = 1
            while Blog.objects.filter(slug=unique_slug).exclude(pk=self.pk).exists():
                unique_slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = str(unique_slug)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return str(self.name)

class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    class Meta:
        ordering = ['-created_at']

    def __str__(self) -> str:
        return str(self.email)