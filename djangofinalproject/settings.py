# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
from pathlib import Path
import os
from datetime import timedelta
from decouple import config
from celery.schedules import crontab

WSGI_APPLICATION = 'djangoexamproject.wsgi.application'

BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG=True
SECRET_KEY = 'your-secret-key123654' 

AUTH_USER_MODEL = 'app.User'

AUTHENTICATION_BACKENDS = [
    'app.backends.CaseInsensitiveModelBackend',  # Replace 'yourapp' with your actual app name
    'django.contrib.auth.backends.ModelBackend',  # Default backend, keep this for fallback
]

# # Celery configuration
CELERY_BROKER_URL = 'redis://djangoexam_redis:6379/0'
CELERY_RESULT_BACKEND = 'redis://djangoexam_redis:6379/0'


# Email configuration

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587  # Use 587 with TLS (recommended for Gmail)
EMAIL_USE_TLS = True  # Set to True for TLS
EMAIL_USE_SSL = False  # Ensure this is False when using TLS
EMAIL_HOST_USER = config('EMAIL_USER')  # Your Gmail address
EMAIL_HOST_PASSWORD = config('EMAIL_PASSWORD')  # Your App Password
DEFAULT_FROM_EMAIL = config('EMAIL_USER')


# Set the default language
LANGUAGE_CODE = 'en'  # Default language code, e.g., 'en' for English, 'fr' for French

# Enable internationalization
# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Baku'

USE_I18N = True

USE_TZ = True

# Define the available languages
LANGUAGES = [
    ('en', 'English'),
    ('az', 'Azərbaycanca'),  # Add other languages you need
    # ('es', 'Spanish'),
    # ('de', 'German'),
]

# Specify the directory where translation files will be stored
LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]


STATIC_URL = '/static/'
ROOT_URLCONF = 'djangoexamproject.urls'

# Determine the host and port based on environment variables, with defaults for local development
POSTGRES_HOST = os.environ.get('POSTGRES_HOST', 'localhost')
POSTGRES_PORT = os.environ.get('POSTGRES_PORT', '5433')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'djangoexamdb',
        'USER': 'admin',
        'PASSWORD': 'admin123',
        'HOST': POSTGRES_HOST,
        'PORT': POSTGRES_PORT,
    }
}

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_simplejwt',
    'app',
    'drf_yasg',  
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'app.middleware.BlockIPMiddleware',  # Add your custom middleware here
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}


SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=7),  # Access token expires in 1 week
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7), # Refresh token expires in 1 week
}


# Configure SWAGGER_SETTINGS for drf_yasg
SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header',
            'description': 'JWT Authorization header using the Bearer scheme. Example: "Bearer {your JWT token}"',
        }
    },
    'USE_SESSION_AUTH': False,  # Ensures the Swagger UI does not prompt for Django's session login
    'JSON_EDITOR': True,        # Enables JSON editor in Swagger UI for complex data structures
    'REFETCH_SCHEMA_WITH_AUTH': True,  # Ensures schema is refetched with authorization headers applied
    'DEFAULT_MODEL_RENDERING': 'example',  # Shows example values for models by default
}

# CELERY_BEAT_SCHEDULE = {
#     'hourly_employee_notification': {
#         'task': 'app.tasks.notify_active_employees_not_registered',
#         'schedule': crontab(minute=0),  # Run at the start of every hour
#     },
# }
#'schedule': crontab(minute=15)  # Runs at every hour on the 15th minute (e.g., 1:15, 2:15, etc.)
#'schedule': crontab(hour=5, minute=0)  # Runs at 5:00 AM every day
#'schedule': crontab(minute='*/2'),  # Run every minute for testing

CELERY_BEAT_SCHEDULE = {
    'daily_employee_notification': {
        'task': 'app.tasks.notify_active_employees_not_registered',
        'schedule': crontab(hour=5, minute=0)  # Runs at 5:00 AM every day
    },
}

LOGGING_DIR = os.path.join(BASE_DIR, 'logs')
if not os.path.exists(LOGGING_DIR):
    os.makedirs(LOGGING_DIR)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'debug.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}