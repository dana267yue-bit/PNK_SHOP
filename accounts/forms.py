import re
from django import forms
from django.forms import inlineformset_factory
from django.contrib.auth.models import User  
from django.core.exceptions import ValidationError

# កែត្រង់នេះ៖ 
# បើបងចង់ប្រើ Product, ProductImage ត្រូវ Import ពី shop.models មិនមែនពី .models ទេ
from shop.models import Product, ProductImage,  Blog 
from .models import UserProfile
from core.models import Slideshow

# ១. Form សម្រាប់បង្កើត និងកែប្រែផលិតផល

# ២. Formset សម្រាប់រូបភាព Gallery បន្ថែម
ProductImageFormSet = inlineformset_factory(
    Product, 
    ProductImage, 
    fields=['image'], 
    extra=3, 
    can_delete=True,
    widgets={'image': forms.FileInput(attrs={'class': 'form-control', 'style': 'border-radius: 8px;'})}
)


# ៣. Form សម្រាប់ស្លាយរូបភាព (Slideshow)
class SlideshowForm(forms.ModelForm):
    class Meta:
        model = Slideshow
        fields = ['title', 'description', 'image', 'link', 'title_color', 'desc_color', 'shadow_color']
        
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control form-control-custom',
                'placeholder': 'បញ្ចូលចំណងជើងស្លាយ...'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control form-control-custom',
                'rows': 3,
                'placeholder': 'បញ្ចូលការពិពណ៌នាសង្ខេប...'
            }),
            'link': forms.URLInput(attrs={
                'class': 'form-control form-control-custom',
                'placeholder': 'ឧទាហរណ៍៖ https://...'
            }),
            'image': forms.FileInput(attrs={
                'class': 'custom-file-input'
            }),
            'title_color': forms.TextInput(attrs={'type': 'color'}),
            'desc_color': forms.TextInput(attrs={'type': 'color'}),
            'shadow_color': forms.TextInput(attrs={'type': 'color'}),
        }


# ៤. Form សម្រាប់ប្លុក (Blog)
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['name', 'slug', 'image', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'បញ្ចូលចំណងជើងប្លុក'}),
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ឧទាហរណ៍: blog-title-1'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'សរសេរខ្លឹមសារប្លុកនៅទីនេះ...'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }


# ៥. Form សម្រាប់ចុះឈ្មោះអ្នកប្រើប្រាស់ (Register)
class SignupForm(forms.ModelForm):

    username = forms.CharField(required=False)
    first_name = forms.CharField(required=True, error_messages={'required': 'សូមបញ្ចូលនាមខ្លួន!'})
    last_name = forms.CharField(required=True, error_messages={'required': 'សូមបញ្ចូលគោត្តនាម!'})
    email = forms.EmailField(required=True, error_messages={'required': 'សូមបញ្ចូលអ៊ីមែល!', 'invalid': 'អ៊ីមែលមិនត្រឹមត្រូវ!'})
    password = forms.CharField(widget=forms.PasswordInput, required=False)
    confirm_password = forms.CharField(widget=forms.PasswordInput, required=False)
    phone = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def clean_username(self):
        username = self.cleaned_data.get("username", "").strip()
        if username and re.match(r'^[a-zA-Z0-9@._+-]+$', username):
            if User.objects.filter(username=username).exists():
                raise ValidationError("ឈ្មោះអ្នកប្រើប្រាស់នេះត្រូវបានប្រើប្រាស់រួចហើយ!")
            return username
        return ""

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if email and User.objects.filter(email=email).exists():
            raise ValidationError("អ៊ីមែលនេះត្រូវបានប្រើប្រាស់រួចហើយ!")
        return email

    def clean_phone(self):
        phone = self.cleaned_data.get("phone")
        if phone and UserProfile.objects.filter(phone=phone).exists():
            raise ValidationError("លេខទូរស័ព្ទនេះត្រូវបានប្រើប្រាស់រួចហើយ!")
        return phone

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password") or self.data.get("password1")
        confirm_password = cleaned_data.get("confirm_password") or self.data.get("password2")

        if not password:
            self.add_error('password', 'សូមបញ្ចូលលេខសម្ងាត់!')
        if not confirm_password:
            self.add_error('confirm_password', 'សូមបញ្ជាក់លេខសម្ងាត់!')

        if password and confirm_password and password != confirm_password:
            raise ValidationError("លេខសម្ងាត់ទាំងពីរមិនផ្ទៀងផ្ទាត់គ្នាទេ!")

        if password:
            cleaned_data['password'] = password
        if confirm_password:
            cleaned_data['confirm_password'] = confirm_password

        # Handle username automatically if empty or non-ASCII (Khmer text)
        raw_username = cleaned_data.get("username", "").strip()
        email = cleaned_data.get("email", "").strip()

        if raw_username and re.match(r'^[a-zA-Z0-9@._+-]+$', raw_username):
            final_username = raw_username
        else:
            base = email.split('@')[0] if '@' in email else 'user'
            base = re.sub(r'[^a-zA-Z0-9@._+-]', '', base) or 'user'
            final_username = base
            counter = 1
            while User.objects.filter(username=final_username).exists():
                final_username = f"{base}_{counter}"
                counter += 1

        cleaned_data['username'] = final_username
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)

        username = self.cleaned_data.get('username')
        if not username:
            username = self.cleaned_data['email']
        user.username = username
        user.email = self.cleaned_data['email']
        user.set_password(self.cleaned_data["password"])

        if commit:
            user.save()

            phone_val = self.cleaned_data.get('phone', '')
            UserProfile.objects.get_or_create(
                user=user,
                defaults={'phone': phone_val}
            )

        return user