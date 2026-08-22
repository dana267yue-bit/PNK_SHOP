from django import forms
from .models import Product, ProductImage
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'brand', 'price', 'category', 'old_price', 'stock', 'image', 'promotion', 'description']
        
        # បន្ថែម Bootstrap class និង Placeholder
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'បញ្ចូលឈ្មោះទូរស័ព្ទ...'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'brand': forms.Select(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': 'ឧទាហរណ៍: 599.00'}),
            'old_price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': 'តម្លៃដើមមុនបញ្ចុះ'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'ចំនួនក្នុងស្តុក'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'promotion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Free Standy, Free Bottle...'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'ព័ត៌មានលម្អិត...'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # ថែមការដេគ័រ border-radius ទៅលើគ្រប់ field ទាំងអស់
        for field_name, field in self.fields.items():
            field.widget.attrs['style'] = 'border-radius: 8px;'
        
        # 🎯 ប្តូរឈ្មោះ Label ជាភាសាខ្មែរឱ្យត្រឹមត្រូវតាមស្ដង់ដារ Django
        labels = {
            'name': 'ឈ្មោះម៉ូដែល/ផលិតផល',
            'category': 'ប្រភេទផលិតផល',
            'brand': 'ម៉ាកយីហោ',
            'price': 'តម្លៃលក់បច្ចុប្បន្ន ($)',
            'old_price': 'តម្លៃដើម ($)',
            'stock': 'ចំនួនក្នុងស្តុក',
            'image': 'រូបភាពចម្បង',
            'promotion': 'ព័ត៌មានបន្ថែម (Promotion)',
            'description': 'ការពិពណ៌នា',
        }
        
        for field_name, label_text in labels.items():
            if field_name in self.fields:
                self.fields[field_name].label = label_text