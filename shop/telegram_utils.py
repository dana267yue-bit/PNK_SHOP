import requests
import os
from django.conf import settings

def send_order_to_telegram(order, items):
    token = '8974537210:AAEgEn5m5xgpwRgrPb5y7sgIHe4MpSDVbNQ'
    chat_id = '5309732054'
    
    payment_methods_map = {
        'cod': 'បង់ប្រាក់ពេលទំនិញទៅដល់ (COD) 💵',
        'khqr': 'ទូទាត់តាម KHQR 📲',
        'online': 'ទូទាត់តាម KHQR 📲',
    }
    payment_str = payment_methods_map.get(order.payment_method, order.payment_method)

    # 1. ព័ត៌មានលម្អិតអំពីការបញ្ជាទិញ (HTML Parse Mode)
    msg = f"🛒 <b><u>ការបញ្ជាទិញថ្មី! #{order.id}</u></b>\n"
    msg += f"━━━━━━━━━━━━━━━━━━━━━\n"
    msg += f"👤 <b>អតិថិជន:</b> {order.last_name} {order.first_name}\n"
    msg += f"📞 <b>ទូរស័ព្ទ:</b> <code>{order.phone}</code>\n"
    if order.email:
        msg += f"📧 <b>អ៊ីមែល:</b> {order.email}\n"
    
    address_parts = [p for p in [order.address_1, order.address_2, order.city] if p]
    if address_parts:
        msg += f"📍 <b>អាសយដ្ឋាន:</b> {', '.join(address_parts)}\n"
        
    msg += f"💳 <b>ការទូទាត់:</b> {payment_str}\n"
    msg += f"⏳ <b>ស្ថានភាព:</b> {order.status}\n"
    
    if order.created_at:
        msg += f"📅 <b>កាលបរិច្ឆេទ:</b> {order.created_at.strftime('%d/%m/%Y %I:%M %p')}\n"
        
    msg += f"\n🛍️ <b><u>មុខទំនិញដែលបានកុម្មង់:</u></b>\n"
    
    total_items_count = 0
    for idx, item in enumerate(items, 1):
        item_total = item.price * item.quantity
        msg += f" {idx}. <b>{item.product.name}</b> (x{item.quantity}) — ${item_total:.2f}\n"
        total_items_count += item.quantity

    msg += f"\n💰 <b><u>ទឹកប្រាក់សរុប:</u></b> <b>${order.total_amount:.2f}</b> ({total_items_count} មុខ)\n"
    
    if order.order_notes:
        msg += f"\n📝 <b>ចំណាំពីអតិថិជន:</b> {order.order_notes}\n"
        
    msg += f"━━━━━━━━━━━━━━━━━━━━━\n"

    # ផ្ញើសារអត្ថបទគោលទៅ Telegram
    url_msg = f"https://api.telegram.org/bot{token}/sendMessage"
    try:
        requests.post(url_msg, data={'chat_id': chat_id, 'text': msg, 'parse_mode': 'HTML'}, timeout=10)
    except Exception as e:
        print(f"Telegram text message error: {e}")

    # ២. ប្រសិនបើមានប័ណ្ណទូទាត់ប្រាក់ (Payment Receipt image) ផ្ញើប័ណ្ណទូទាត់ប្រាក់
    if order.payment_receipt:
        try:
            receipt_path = os.path.join(settings.MEDIA_ROOT, order.payment_receipt.name)
            if os.path.exists(receipt_path):
                url_photo = f"https://api.telegram.org/bot{token}/sendPhoto"
                with open(receipt_path, 'rb') as photo:
                    payload = {
                        'chat_id': chat_id,
                        'caption': f"🧾 <b>រូបភាពប័ណ្ណទូទាត់ប្រាក់ (Receipt)</b> សម្រាប់ការកុម្មង់ #{order.id}",
                        'parse_mode': 'HTML'
                    }
                    requests.post(url_photo, data=payload, files={'photo': photo}, timeout=10)
        except Exception as e:
            print(f"Telegram receipt error: {e}")

    # ៣. ផ្ញើរូបភាពទំនិញនីមួយៗ
    for item in items:
        if item.product and item.product.image:
            try:
                image_path = os.path.join(settings.MEDIA_ROOT, item.product.image.name)
                if os.path.exists(image_path):
                    url_photo = f"https://api.telegram.org/bot{token}/sendPhoto"
                    with open(image_path, 'rb') as photo:
                        payload = {
                            'chat_id': chat_id,
                            'caption': f"📦 <b>{item.product.name}</b>\nចំនួន: {item.quantity} | តម្លៃ: ${item.price:.2f}",
                            'parse_mode': 'HTML'
                        }
                        requests.post(url_photo, data=payload, files={'photo': photo}, timeout=10)
            except Exception as e:
                print(f"Telegram item photo error: {e}")