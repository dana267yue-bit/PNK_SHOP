from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from allauth.socialaccount.signals import pre_social_login
from .models import UserProfile  # ហៅចេញពី __init__.py នៃ folder models ដែលយើងបានរៀបចំ


# 1. ប្រព័ន្ធបង្កើត USER PROFILE អូតូ (ប្រើ get_or_create គឺសុវត្ថិភាពបំផុត)
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.get_or_create(user=instance)


# 2. ប្រព័ន្ធ GOOGLE LOGIN SIGNAL (ភ្ជាប់គណនីអូតូ និងបង្កើត Username មិនឱ្យជាន់គ្នា)
@receiver(pre_social_login)
def save_google_user_data(sender, request, sociallogin, **kwargs):
    email = sociallogin.user.email
    first_name = sociallogin.user.first_name
    last_name = sociallogin.user.last_name

    # ឆែកមើលថាតើមាន Email ហ្នឹងក្នុងប្រព័ន្ធហើយឬនៅ
    user = User.objects.filter(email=email).first()

    if user:
        # បើមានហើយ ភ្ជាប់គណនី Google ទៅកាន់ User ចាស់នោះភ្លាម
        sociallogin.connect(request, user)
        UserProfile.objects.get_or_create(user=user)
        return

    # បង្កើត Unique Username ការពារកុំឱ្យជាន់គ្នាទាក់ Error Database
    base_username = email.split('@')[0]
    username = base_username
    counter = 1

    while User.objects.filter(username=username).exists():
        username = f"{base_username}{counter}"
        counter += 1

    # រក្សាទុកព័ត៌មានរបស់ User ថ្មី
    sociallogin.user.username = username
    sociallogin.user.email = email
    sociallogin.user.first_name = first_name or ""
    sociallogin.user.last_name = last_name or ""