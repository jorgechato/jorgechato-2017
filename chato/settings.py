import os
import dj_database_url


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = os.getenv('DEBUG', False) == 'True'

ALLOWED_HOSTS = [
    "*",
    "0.0.0.0",
    "localhost",
    "backend",
    "jorgechato.com",
]

SITE_ID = 1

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'compressor',
    'import_export',
    'robots',
    'ckeditor',
    'ckeditor_uploader',
    'imagekit',

    'posts',
    'work',
    'events',
    'home',
]

if DEBUG:
    INSTALLED_APPS += [
        'django_extensions',
        'autofixture',
    ]
    pass

MIDDLEWARE = [
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'chato.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'work.context_processors.header',
            ],
        },
    },
]


# Password validation
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

# Ckeditor config
CKEDITOR_CONFIGS = {
    'default': {
        'skin': 'moono-lisa',
        "codeSnippet_theme": "github",
        'toolbar_OrggueToolbar': [
                {'name': 'document', 'items': ['Source']},
                {'name': 'links', 'items': ['Link', 'Unlink']},
                {'name': 'insert', 'items': [
                    'CodeSnippet', 'Iframe', 'Image']},
                {'name': 'colors', 'items': ['TextColor', 'BGColor']},
                {'name': 'tools', 'items': ['Maximize', 'ShowBlocks']},
                {'name': 'styles', 'items': ['Styles', 'Format', 'FontSize']},
                {'name': 'basicstyles', 'items': [
                    'Bold', 'Italic', 'Underline', 'Strike',
                    'Subscript', 'Superscript', '-', 'RemoveFormat']},
                {'name': 'paragraph', 'items': [
                    'NumberedList', 'BulletedList', '-', 'Outdent',
                    'Indent', '-', 'Blockquote', 'CreateDiv', '-',
                    'JustifyLeft', 'JustifyCenter', 'JustifyRight',
                    'JustifyBlock', '-', 'BidiLtr', 'BidiRtl']},
        ],
        'toolbar': 'OrggueToolbar',
        'tabSpaces': 4,
        'allowedContent': True,
        'extraPlugins': ','.join(
            [
                'codesnippet',
                'iframe',
                'autolink',
            ]),
    }
}
CKEDITOR_UPLOAD_SLUGIFY_FILENAME = True
CKEDITOR_ALLOW_NONIMAGE_FILES = False


# Internationalization
LANGUAGE_CODE = 'es'

TIME_ZONE = 'Europe/Madrid'

USE_I18N = True

USE_L10N = True

USE_TZ = True


COMPRESS_PRECOMPILERS = (
    ('text/x-sass', 'django_libsass.SassCompiler'),
    ('text/x-scss', 'django_libsass.SassCompiler'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # other finders..
    'compressor.finders.CompressorFinder',
)

COMPRESS_CSS_FILTERS = (
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter',
)

COMPRESS_ENABLED = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
COMPRESS_URL = STATIC_URL

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'staticfiles'),
)

CKEDITOR_UPLOAD_PATH = "uploads/"
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
COMPRESS_ROOT = STATIC_ROOT

email = os.environ.get('email')

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('POSTGRES_DB'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': os.getenv('DATABASE_HOST', 'localhost'),
        'PORT': '',
    }
}
if os.environ.get('DATABASE_URL'):
    DATABASES['default'] = dj_database_url.config()
