from django import forms
from django.forms import inlineformset_factory
from .models import Product, ProductImage,Slideshow
from .models import Blog
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'brand', 'price', 'stock', 'image', 'description']
        
        # បន្ថែម Bootstrap class និង Placeholder ឱ្យមើលទៅស្អាត
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'បញ្ចូលឈ្មោះទូរស័ព្ទ'}),
            'brand': forms.Select(attrs={'class': 'form-control'}), 
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'ឧទាហរណ៍: 599.00'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'ចំនួនក្នុងស្តុក'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'ព័ត៌មានលម្អិត...'}),
        }
        
        # ប្តូរឈ្មោះ Label ជាភាសាខ្មែរ
        labels = {
            'name': 'ឈ្មោះម៉ូដែល',
            'brand': 'ម៉ាកយីហោ',
            'price': 'តម្លៃលក់ ($)',
            'stock': 'ចំនួនក្នុងស្តុក',
            'image': 'រូបភាពចម្បង',
            'description': 'ការពិពណ៌នា',
        }

# Formset សម្រាប់រូបភាព Gallery បន្ថែម
ProductImageFormSet = inlineformset_factory(
    Product, 
    ProductImage, 
    fields=['image'], 
    extra=3, 
    can_delete=True,
    widgets={'image': forms.FileInput(attrs={'class': 'form-control'})}
)


class SlideshowForm(forms.ModelForm):
    class Meta:
        model = Slideshow
        fields = ['title', 'image', 'link']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'បញ្ចូលចំណងជើង'}),
            'image': forms.FileInput(attrs={'class': 'custom-file-input'}),
            'link': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://...'}),
        }



class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'slug', 'image', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'បញ្ចូលចំណងជើងប្លុក'}),
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ឧទាហរណ៍: blog-title-1'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'សរសេរខ្លឹមសារប្លុកនៅទីនេះ...'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

# ក្នុង forms.py
class RegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})