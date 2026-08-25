import os
from pathlib import Path

try:
    import dj_database_url
except ImportError:
    dj_database_url = None

BASE_DIR = Path(__file__).resolve().parent.parent

# =========================================
# SECURITY
# =========================================
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-_uwaqr#==_2_ua)iq(v7z4')

DEBUG = os.environ.get('DEBUG', 'True') == 'True'

ALLOWED_HOSTS = ['*']

CSRF_TRUSTED_ORIGINS = [
    'https://*.onrender.com',
    'https://pnk-shop-5zfw.onrender.com',
    'https://pnk-shop.onrender.com',
    'http://127.0.0.1:8000',
    'http://localhost:8000',
]


# =========================================
# INSTALLED APPS
# =========================================
INSTALLED_APPS = [

    # Django Apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # Third Party Apps
    'widget_tweaks',

    # Allauth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',

    # Your Apps
    'accounts.apps.AccountsConfig',
    'shop',
    'core',
]

SITE_ID = 2


# =========================================
# MIDDLEWARE
# =========================================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
]

try:
    import whitenoise  # noqa: F401
    MIDDLEWARE.append('whitenoise.middleware.WhiteNoiseMiddleware')
except ImportError:
    pass

MIDDLEWARE += [
    'django.contrib.sessions.middleware.SessionMiddleware',

    'django.middleware.common.CommonMiddleware',

    'django.middleware.csrf.CsrfViewMiddleware',

    'django.contrib.auth.middleware.AuthenticationMiddleware',

    'django.contrib.messages.middleware.MessageMiddleware',

    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # ALLAUTH
    'allauth.account.middleware.AccountMiddleware',

    # Admin / Staff 30-min Inactivity Idle Timeout Middleware
    'accounts.middleware.AdminSessionIdleTimeoutMiddleware',
]

X_FRAME_OPTIONS = 'SAMEORIGIN'


# =========================================
# ROOT URL
# =========================================
ROOT_URLCONF = 'PNK.urls'


# =========================================
# TEMPLATES
# =========================================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        'DIRS': [
            BASE_DIR / 'templates'
        ],

        'APP_DIRS': True,

        'OPTIONS': {
            'context_processors': [

                'django.template.context_processors.debug',

                'django.template.context_processors.request',

                'django.contrib.auth.context_processors.auth',

                'django.contrib.messages.context_processors.messages',

                'accounts.context_processors.cart_context',
                'accounts.context_processors.dashboard_notifications',
                'accounts.context_processors.store_settings_context',
            ],
        },
    },
]


# =========================================
# WSGI
# =========================================
WSGI_APPLICATION = 'PNK.wsgi.application'


# =========================================
# DATABASE
# =========================================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

DATABASE_URL = os.environ.get('DATABASE_URL')
if DATABASE_URL and dj_database_url:
    DATABASES['default'] = dj_database_url.config(default=DATABASE_URL, conn_max_age=600)


# =========================================
# PASSWORD VALIDATORS
# =========================================
AUTH_PASSWORD_VALIDATORS = [

    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },

    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },

    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },

    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# =========================================
# AUTHENTICATION
# =========================================
AUTHENTICATION_BACKENDS = [

    'django.contrib.auth.backends.ModelBackend',

    'allauth.account.auth_backends.AuthenticationBackend',
]


# =========================================
# LOGIN / LOGOUT
# =========================================
LOGIN_URL = '/auth/login/'

LOGIN_REDIRECT_URL = '/'

LOGOUT_REDIRECT_URL = '/auth/login/'


# =========================================
# ALLAUTH SETTINGS
# =========================================
ACCOUNT_LOGIN_METHODS = {'username', 'email'}

ACCOUNT_SIGNUP_FIELDS = ['email*', 'username*', 'password1*', 'password2*']

ACCOUNT_EMAIL_VERIFICATION = 'none'

ACCOUNT_LOGIN_ON_SIGNUP = True

SOCIALACCOUNT_LOGIN_ON_GET = True

ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'https' if not DEBUG else 'http'
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

SOCIALACCOUNT_EMAIL_AUTHENTICATION = True
SOCIALACCOUNT_AUTO_SIGNUP = True

# =========================================
# GOOGLE LOGIN
# =========================================
GOOGLE_CLIENT_ID = os.environ.get('GOOGLE_CLIENT_ID')
GOOGLE_CLIENT_SECRET = os.environ.get('GOOGLE_CLIENT_SECRET')

SOCIALACCOUNT_PROVIDERS = {

    'google': {

        'SCOPE': [
            'profile',
            'email',
        ],

        'AUTH_PARAMS': {
            'access_type': 'online',
        },

        'OAUTH_PKCE_ENABLED': True,
    }
}

if GOOGLE_CLIENT_ID and GOOGLE_CLIENT_SECRET:
    SOCIALACCOUNT_PROVIDERS['google']['APP'] = {
        'client_id': GOOGLE_CLIENT_ID,
        'secret': GOOGLE_CLIENT_SECRET,
        'key': ''
    }


# =========================================
# EMAIL CONFIG
# =========================================
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'smtp.gmail.com'

EMAIL_PORT = 587

EMAIL_USE_TLS = True

EMAIL_HOST_USER = 'dana267yue@gmail.com'

EMAIL_HOST_PASSWORD = 'dubkkndupqukpmzh'

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER


# =========================================
# PASSWORD RESET
# =========================================
ACCOUNT_FORMS = {
    'reset_password': 'allauth.account.forms.ResetPasswordForm',
}


# =========================================
# LANGUAGE
# =========================================
LANGUAGE_CODE = 'km'

TIME_ZONE = 'Asia/Phnom_Penh'

USE_I18N = True

USE_TZ = True


# =========================================
# STATIC FILES
# =========================================
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

STATIC_ROOT = BASE_DIR / 'staticfiles'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
WHITENOISE_MANIFEST_STRICT = False


# =========================================
# MEDIA FILES
# =========================================
MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR / 'media'


# =========================================
# UPLOAD LIMIT
# =========================================
DATA_UPLOAD_MAX_MEMORY_SIZE = 5 * 1024 * 1024


# =========================================
# DEFAULT AUTO FIELD
# =========================================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# =========================================
# SESSION SETTINGS
# =========================================
# Session នឹងត្រូវលុបចោលភ្លាមៗពេល Browser ត្រូវបានបិទទាំងស្រុង
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
