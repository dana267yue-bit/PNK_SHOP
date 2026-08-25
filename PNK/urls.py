from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# បន្ថែមបន្ទាត់នេះ៖
from allauth.account.views import LoginView 

urlpatterns = [
   path('admin/', admin.site.urls),
   path('auth/', include('allauth.urls')),    
   path('accounts/', include('accounts.urls')),
   path('', include('core.urls')),
   path('shop/', include('shop.urls', namespace='shop')),       
   # ឥឡូវនេះវាស្គាល់ LoginView ហើយ
   path('auth/login/', LoginView.as_view(), name='login'),     
]

from django.urls import re_path
from django.views.static import serve

urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]