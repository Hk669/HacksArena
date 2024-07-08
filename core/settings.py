from pathlib import Path
import os
from dotenv import load_dotenv
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('SECRET_KEY')
if not SECRET_KEY:
    raise ValueError("The SECRET_KEY setting must not be empty.")
# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = False
DEBUG = True


ALLOWED_HOSTS = ['127.0.0.1:8000','127.0.0.1','*.onrender.com','event.hrushikesh.xyz']

AUTH_USER_MODEL = 'main.User'

SITE_ID = 3     # created 1 extra site (example.com)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend'
)


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "whitenoise.runserver_nostatic",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    
    # installed apps
    'main',
    'corsheaders',
    #share links
    'django_social_share',

    #blog editor
    'ckeditor',

    # for allauth
    'rest_framework',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.github',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware"
]


# CORS_ALLOWED_ORIGINS = [
#     "https://hacksarena.azurewebsites.net",

# ]

# account providers (google, github)
SOCIALACCOUNT_PROVIDERS = {
    'google' : {
        'SCOPE' : [
            'profile',
            'email'
        ],
        'AUTH_PARAMS' : {
            'access_type' : 'online'
        }
    },

    'github' : {
        'SCOPE' : [
            'read:user',
            'user:email',
        ],

        # 'APP' : {
        #     'client_id' : os.environ.get('CLIENT_ID'),
        #     'secret' : os.environ.get("SECRET_GITHUB"),
        #     'key' : ''
        # }
    }
}

# SOCIAL_AUTH_GOOGLE_OAUTH2_CALLBACK_URL = 'https://hacksarena.azurewebsites.net/accounts/google/login/callback/'


ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / 'templates'
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 300,
        'width': 800,
    },
}


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# Azure postgres SQl database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "postgres",
        "USER": os.environ.get('USER'),
        "PASSWORD": os.environ.get("DBPASSWORD"),
        "HOST": os.environ.get('HOST'),
        "PORT": "5432",
        "OPTIONS" : {
            "sslmode": "require"
        }
    }
}

#default
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / "db.sqlite3",
#     }
# }



# Redis cache

CACHE_TTL = 20 * 1500  #( time cache exists)

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': os.getenv('REDIS_URI'),
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        },
    }
}

# Set your Redis password as an environment variable
# REDIS_PASSWORD = os.environ.get('REDIS_PASSWORD')

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

# indian time
TIME_ZONE = "Asia/Kolkata"

USE_I18N = True
USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


LOGOUT_REDIRECT_URL = '/'
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/login/'


SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
# CSRF_COOKIE_DOMAIN = 'hacksarena.azurewebsites.net'


# s3 buckets for images upload
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
AWS_S3_REGION_NAME = 'us-east-1'  
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
AWS_S3_SIGNATURE_VERSION = 's3v4'
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None  # Recommended to prevent setting public ACL by default
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',  # Set cache control headers
}

# For serving static files directly from S3
AWS_S3_USE_SSL = True
AWS_S3_VERIFY = True
AWS_S3_URL = "https://assests.hacksarena.s3.amazonaws.com/"

STATIC_URL = "https://assests.hacksarena.s3.amazonaws.com/static/"
MEDIA_URL = "https://assests.hacksarena.s3.amazonaws.com/media/"
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
