from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone = models.CharField(max_length=20, blank=True, null=True)
    image = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    objects = models.Manager()

class Slideshow(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True) # ថែមនេះ
    image = models.ImageField(upload_to='slideshows/')
    link = models.URLField(max_length=500, blank=True, null=True)
    
    # --- ផ្នែកសម្រាប់ស្ទីល (Styling) ---
    title_color = models.CharField(max_length=10, default="#ffffff") # ពណ៌ចំណងជើង
    desc_color = models.CharField(max_length=10, default="#e0e0e0")  # ពណ៌ការពិពណ៌នា
    shadow_color = models.CharField(max_length=10, default="rgba(0,0,0,0.5)") # ពណ៌ស្រមោល
    objects = models.Manager()

class ActivityLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    action = models.CharField(max_length=255)
    details = models.TextField(blank=True, null=True)
    icon = models.CharField(max_length=50, default="bi-info-circle")
    color_class = models.CharField(max_length=50, default="text-info")
    created_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    class Meta:
        ordering = ['-created_at']

    def __str__(self) -> str:
        date_str = self.created_at.strftime('%Y-%m-%d %H:%M') if hasattr(self.created_at, 'strftime') else str(self.created_at)
        return f"{self.action} ({date_str})"


class StoreSetting(models.Model):
    store_name = models.CharField(max_length=255, default="PNK SHOP")
    phone = models.CharField(max_length=50, default="096 29 647 13")
    email = models.EmailField(default="dana267yue@gmail.com")
    currency = models.CharField(max_length=10, default="USD")
    address = models.CharField(max_length=500, default="ភូមិនិគមន៍លើ ខេត្តត្បូងឃ្មុំ, ព្រះរាជាណាចក្រកម្ពុជា")
    facebook_link = models.URLField(max_length=500, default="https://facebook.com/pnkmobile", blank=True, null=True)
    telegram_link = models.URLField(max_length=500, default="https://t.me/pnkmobile", blank=True, null=True)
    logo = models.ImageField(upload_to='store/', null=True, blank=True)
    map_iframe = models.TextField(blank=True, null=True)
    chat_auto_reply = models.TextField(default="សូមអរគុណសម្រាប់ការផ្ញើសារ! ក្រុមការងារ PNK SHOP បានទទួលសាររបស់អ្នកហើយ។ លោកអ្នកក៏អាចឆាតផ្ទាល់តាម Telegram:", blank=True, null=True)
    enable_auto_reply = models.BooleanField(default=False)

    # Quick Questions & Answers in Live Chat
    chat_quick_tradein_q = models.CharField(max_length=255, default="🔄 សួរអំពីការប្តូរចាស់យកថ្មី (Trade-In)?", blank=True, null=True)
    chat_quick_tradein_a = models.TextField(default="🔄 <strong>សេវាកម្ម ប្តូរចាស់យកថ្មី (Trade-In)</strong>៖<br>• វាយតម្លៃទូរស័ព្ទចាស់បានតម្លៃខ្ពស់សមរម្យ<br>• ថែមប្រាក់តិចតួចយកស៊េរីថ្មីភ្លាមៗ<br>👉 សូមផ្ញើ <strong>ម៉ូឌែលទូរស័ព្ទចាស់ + ស្ថានភាព (ស្អាត/ឆ្កូត)</strong> មកកាន់ទីនេះ ឬទាក់ទងមក Admin ដើម្បីវាយតម្លៃភ្លាមៗបាទ/ចាស! 📱✨", blank=True, null=True)
    
    chat_quick_installment_q = models.CharField(max_length=255, default="💳 សួរអំពីការបង់រំលស់ 5%?", blank=True, null=True)
    chat_quick_installment_a = models.TextField(default="💳 <strong>សេវាកម្ម បង់រំលស់ងាយៗ</strong>៖<br>• ការប្រាក់ចាប់ពី 0% ដល់ 5% ឯកសារងាយៗ<br>• អនុម័តរហ័សក្នុងរយៈពេល ១៥-៣០ នាទី<br>• ឯកសារ៖ អត្តសញ្ញាណប័ណ្ណ + សៀវភៅគ្រួសារ/ស្នាក់នៅ + លិខិតបញ្ជាក់ប្រាក់ខែ<br>👉 សូមផ្ញើ <strong>ម៉ូឌែលទូរស័ព្ទដែលចង់បាន</strong> មកកាន់ទីនេះដើម្បីឱ្យ Admin ជួយគណនាប្រាក់បង់ប្រចាំខែជូនបាទ/ចាស! 📱✨", blank=True, null=True)
    
    chat_quick_hours_q = models.CharField(max_length=255, default="🕒 តើហាងបើកលក់ម៉ោងប៉ុន្មាន?", blank=True, null=True)
    chat_quick_hours_a = models.TextField(default="ហាង <strong>PNK SHOP</strong> បើកបម្រើអតិថិជនរៀងរាល់ថ្ងៃ ពីម៉ោង <strong>7:30 ព្រឹក ដល់ 8:30 យប់</strong>! អាចអញ្ជើញមកផ្ទាល់ ឬកុម្មង់តាមអនឡាញបានរហ័ស។ 🕒", blank=True, null=True)
    
    chat_quick_shipping_q = models.CharField(max_length=255, default="🚚 តើមានសេវាដឹកជញ្ជូន ២៤ ខេត្តក្រុងទេ?", blank=True, null=True)
    chat_quick_shipping_a = models.TextField(default="យើងខ្ញុំមានសេវាដឹកជញ្ជូនរហ័សទាន់ចិត្ត និងសុវត្ថិភាព ដល់ដៃអតិថិជននៅគ្រប់ <strong>២៤ ខេត្តក្រុង</strong> ទូទាំងប្រទេសកម្ពុជា! 📦🚚", blank=True, null=True)

    objects = models.Manager()

    @classmethod
    def get_settings(cls):
        settings_obj, created = cls.objects.get_or_create(id=1)
        return settings_obj

    def __str__(self) -> str:
        return str(self.store_name)


class ChatMessage(models.Model):
    SENDER_CHOICES = (('customer', 'Customer'), ('admin', 'Admin'))
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chat_messages')
    sender = models.CharField(max_length=20, choices=SENDER_CHOICES, default='customer')
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    class Meta:
        ordering = ['created_at']

    def __str__(self) -> str:
        return f"{self.user.username} ({self.sender}): {self.message[:30]}"
