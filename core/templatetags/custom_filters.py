from django import template

register = template.Library()

@register.filter(name='calculate_discount')
def calculate_discount(old_price, price):
    try:
        # ការពារករណីគ្មានតម្លៃ ឬតម្លៃចាស់ស្មើ ០ ឬតិចជាងតម្លៃថ្មី
        if not old_price or not price or old_price <= price:
            return 0
        
        # រូបមន្តគណនាភាគរយបញ្ចុះតម្លៃ៖ ((តម្លៃចាស់ - តម្លៃថ្មី) / តម្លៃចាស់) * ១០០
        discount = ((old_price - price) / old_price) * 100
        return int(round(discount))  # បំប្លែងជាចំនួនគត់ (ឧទាហរណ៍៖ 7% ឬ 10%)
    except (ValueError, ZeroDivisionError):
        return 0

@register.filter(name='sub')
def sub(value, arg):
    try:
        res = float(value) - float(arg)
        if res.is_integer():
            return int(res)
        return round(res, 2)
    except (ValueError, TypeError):
        return 0