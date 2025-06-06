"""
Django settings for kanzlei_backend project.

Generated by 'django-admin startproject' using Django 5.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.2/ref/settings/
"""

from pathlib import Path
from datetime import timedelta
from corsheaders.defaults import default_headers, default_methods # Import default headers and methods for CORS

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure--ad4&@lbfx%lqai=nkus&pgf8wh(wp7p*odqc1gfr%1jk5zws7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '0.0.0.0'
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_simplejwt',                     # JWT authentication
    'rest_framework_simplejwt.token_blacklist',     # JWT token blacklist for Simple JWT
    'rest_framework.authtoken',
    'corsheaders',                                  # Add CORS headers support
    'kanzlei_apps.accounts',                        # Your accounts app
    'kanzlei_apps.cases',                           # Your cases app
    'kanzlei_apps.appointments',                    # Your appointments app
    'kanzlei_apps.users',                           # Your users app
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.locale.LocaleMiddleware',    # For internationalization
]

ROOT_URLCONF = 'kanzlei_backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'kanzlei_backend.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

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

# Custom user model settings
# https://docs.djangoproject.com/en/5.2/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project
# If you have a custom user model, specify it here
# This should be the app label and the model name, e.g., 'users.User'
# If you have a custom user model, ensure it is defined in your app
# 'users' is the app name and 'User' is the model name
# https://docs.djangoproject.com/en/5.2/topics/auth/customizing/#specifying-a-custom-user-model
AUTH_USER_MODEL = 'users.User'

# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'
# Ensure the static files are served correctly in production
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

# Media files (user-uploaded content)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
# Rest framework settings
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}

# Caching settings
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
        'TIMEOUT': 300,                 # Cache timeout in seconds
        'OPTIONS': {
            'MAX_ENTRIES': 1000,        # Maximum number of entries in the cache
        },
    }
}

# Security settings
# SECURE_BROWSER_XSS_FILTER = True
# SECURE_CONTENT_TYPE_NOSNIFF = True
# SECURE_HSTS_SECONDS = 3600              # Enable HTTP Strict Transport Security for 1 hour
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True   # Include subdomains in HSTS
# SECURE_HSTS_PRELOAD = True              # Preload HSTS for browsers
# SECURE_SSL_REDIRECT = True              # Redirect all HTTP requests to HTTPS

# Session settings
# SESSION_COOKIE_SECURE = True            # Use secure cookies for sessions
# SESSION_COOKIE_SAMESITE = 'Lax'         # Adjust as needed for your application

# CORS settings
# Configure CORS headers
CORS_ALLOW_ALL_ORIGINS = True           # Uncomment if you want to allow all origins (not recommended for production)
CORS_ORIGIN_ALLOW_ALL = True            # Set to True if you want to allow all origins (not recommended for production)
CORS_ALLOW_CREDENTIALS = True           # Allow cookies to be included in CORS requests
CORS_ALLOW_HEADERS = list(default_headers) + [
    'X-CSRFToken',                      # Allow CSRF token header
]
CORS_ALLOWED_ORIGINS = []
# CORS_ALLOW_METHODS = [
#     'GET',
#     'POST',
#     'PUT',
#     'PATCH',
#     'DELETE', 
#     'OPTIONS'
# ]                                       # Uncomment if you need to restrict methods
CORS_ALLOW_METHODS = list(default_methods)  # Uncomment if you want to use default methods

# CSRF settings
# CSRF_COOKIE_SECURE = True               # Use secure cookies for CSRF
# CSRF_COOKIE_SAMESITE = 'Lax'            # Adjust as needed for your application
CSRF_TRUSTED_ORIGINS = [
    'http://localhost:3000',            # Adjust this to your frontend URL
    "http://localhost:4200",            # Angular app running on localhost
]

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# JWT settings
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
}