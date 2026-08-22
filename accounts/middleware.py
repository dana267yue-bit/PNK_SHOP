import time
from django.contrib.auth import logout
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse
from django.http import JsonResponse

class AdminSessionIdleTimeoutMiddleware:
    """
    Middleware សម្រាប់គ្រប់គ្រង Session Timeout ដោយស្វ័យប្រវត្តិចំពោះ Admin និង Staff៖
    ប្រសិនបើ Admin/Staff អសកម្ម (គ្មានសកម្មភាព) លើសពី 30 នាទី (1800 វិនាទី)
    ប្រព័ន្ធនឹងផ្ដាច់ Session ដោយស្វ័យប្រវត្តិ ហើយតម្រូវឱ្យ Login ឡើងវិញ។
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated and (request.user.is_staff or request.user.is_superuser):
            current_time = int(time.time())
            last_activity = request.session.get('admin_last_activity')
            timeout_seconds = 1800  # 30 នាទី

            # ពិនិត្យមើលថាតើ Session ផុតកំណត់ដោយសារអសកម្មដែរឬទេ
            if last_activity and (current_time - last_activity > timeout_seconds):
                logout(request)
                # សម្អាត session key
                if 'admin_last_activity' in request.session:
                    del request.session['admin_last_activity']

                # បើជា AJAX / API request
                if request.headers.get('x-requested-with') == 'XMLHttpRequest' or request.path.startswith('/accounts/api/'):
                    return JsonResponse({
                        'status': 'session_expired',
                        'message': 'Session របស់អ្នកបានផុតកំណត់ដោយសារគ្មានសកម្មភាពលើសពី ៣០ នាទី។ សូម Login ឡើងវិញ!'
                    }, status=401)

                messages.warning(
                    request,
                    "Session របស់អ្នកបានផុតកំណត់ដោយសារគ្មានសកម្មភាពលើសពី ៣០ នាទី។ សូម Login ឡើងវិញដើម្បីបន្ត!"
                )
                return redirect('account_login')

            # កុំ update activity ពេលមានតែ background polling API
            background_polling_paths = [
                '/accounts/api/get-latest-messages/',
                '/accounts/api/get-customer-chat-history/',
            ]
            if request.path not in background_polling_paths:
                request.session['admin_last_activity'] = current_time

        response = self.get_response(request)
        return response
