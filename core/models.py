from django.db import models

class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True # 🚀 បញ្ជាក់ថាជាម៉ូដែលគ្រឹះ (មិនបង្កើតតារាងផ្ទាល់ខ្លួនទេ)

from django.db import models

# ១. បង្កើត Model Brand
class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# ២. បង្កើត Model Product ដែលភ្ជាប់ជាមួយ Brand
class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    old_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True) # បន្ថែមនេះ
    image = models.ImageField(upload_to='products/')
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE) # សន្មតថាមាន Brand model
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

# ក្នុង accounts/models.py
class Slideshow(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True) # បន្ថែមនេះ
    image = models.ImageField(upload_to='slideshows/')
    link = models.URLField(blank=True, null=True)        # បន្ថែមនេះ
    title_color = models.CharField(max_length=7, default="#000000") # បន្ថែមនេះ
    desc_color = models.CharField(max_length=7, default="#000000")
    shadow_color = models.CharField(max_length=7, default="#000000")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title if self.title else f"Slide {self.id}"

# ៤. TimestampedModel (សម្រាប់ប្រើប្រាស់បន្ត)
class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True