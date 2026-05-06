from django.db import models
from django.utils.text import slugify

# ១. ម៉ូដែលសម្រាប់ប្រភេទផលិតផល (Categories)
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="ឈ្មោះប្រភេទ")
    image = models.ImageField(upload_to='categories/', null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True)

    class Meta:
        verbose_name_plural = "Categories" # ដើម្បីឱ្យវាកុំលោតអក្សរ Categorys (ខុសអក្ខរាវិរុទ្ធអង់គ្លេស)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

# ២. ម៉ូដែលសម្រាប់ម៉ាក (Brands)
class Brand(models.Model):
    name = models.CharField(max_length=100, verbose_name="ឈ្មោះម៉ាក")
    logo = models.ImageField(upload_to='brands/', null=True, blank=True)

    def __str__(self):
        return self.name

# ៣. ម៉ូដែលសម្រាប់ផលិតផល (Products) - រួមបញ្ចូលរាល់ Field ទាំងអស់
class Product(models.Model):
    # បន្ថែមបន្ទាត់នេះ (សំខាន់បំផុត)
    title = models.CharField(max_length=255, verbose_name="ឈ្មោះផលិតផល", default="មិនទាន់ដាក់ឈ្មោះ")
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', null=True, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True, related_name='products')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="តម្លៃ")
    description = models.TextField(blank=True, null=True, verbose_name="ការពិពណ៌នា")
    image = models.ImageField(upload_to='products/', blank=True, null=True, verbose_name="រូបភាពចម្បង")
    stock = models.IntegerField(default=0, verbose_name="ចំនួនក្នុងស្តុក")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products/gallery/')

    def __str__(self):
        return f"Image for {self.product.name}"

# ៥. ម៉ូដែលសម្រាប់ស្លាយរូបភាព (Slideshow)
class Slideshow(models.Model):
    title = models.CharField(max_length=200, verbose_name="ចំណងជើង")
    sub_title = models.CharField(max_length=200, blank=True, verbose_name="ចំណងជើងរង")
    image = models.ImageField(upload_to='slideshows/', verbose_name="រូបភាព")
    link = models.URLField(blank=True, null=True, verbose_name="តំណភ្ជាប់ (URL)")
    is_active = models.BooleanField(default=True, verbose_name="បង្ហាញលើ Web")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# ៦. ម៉ូដែលសម្រាប់ប្លុក (Blog)
class Blog(models.Model):
    title = models.CharField(max_length=255, verbose_name="ចំណងជើងអត្ថបទ")
    slug = models.SlugField(unique=True, blank=True, null=True)
    image = models.ImageField(upload_to='blog_images/', verbose_name="រូបភាព")
    description = models.TextField(verbose_name="ខ្លឹមសារ")
    date_added = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title