import os
from pathlib import Path
from dotenv import load_dotenv, find_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv('.env')

SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = os.getenv('DEBUG')

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS').split(',')

INSTALLED_APPS = [
    "jazzmin",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "apps.shared.apps.SharedConfig",
    "rest_framework",
    "drf_spectacular",
    "drf_spectacular_sidecar",
    "apps.clickpayment",
    "clickuz",
    'django_ckeditor_5',
    'parler',
    'rosetta',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = "core.wsgi.application"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
    }
}

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

REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

SPECTACULAR_SETTINGS = {
    "SWAGGER_UI_DIST": "SIDECAR",
    "SWAGGER_UI_FAVICON_HREF": "SIDECAR",
    "REDOC_DIST": "SIDECAR",
    "TITLE": "Django Rest API",
}

CLICK_SETTINGS = {
    "service_id": os.getenv("CLICK_SERVICE_ID"),
    "merchant_id": os.getenv("CLICK_MERCHANT_ID"),
    "secret_key": os.getenv("CLICK_SECRET_KEY"),
    "merchant_user": os.getenv("CLICK_MERCHANT_USER_ID"),
}

LANGUAGE_CODE = 'en'
LANGUAGES = [
    ('en', 'English'),
    ('ru', 'Russian'),  # Added Russian
]

TIME_ZONE = 'Asia/Tashkent'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = [
    os.path.join(BASE_DIR, "locale")
]
PARLER_DEFAULT_LANGUAGE_CODE = 'en'
PARLER_LANGUAGES = {
    None: (
        {'code': 'en', },
        {'code': 'ru', },
    ),
    'default': {
        'fallback': 'en',  # defaults to PARLER_DEFAULT_LANGUAGE_CODE
        'hide_untranslated': False,  # the default; let .active_translations() return fallbacks too.
    }
}
STATIC_URL = '/apps/static/'
STATIC_ROOT = os.path.join(BASE_DIR / 'apps/static')
# STATICFILES_DIRS = os.path.join(BASE_DIR / "static")
MEDIA_URL = 'apps/media/'
MEDIA_ROOT = os.path.join(BASE_DIR / 'apps/media')
CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_IMAGE_BACKEND = 'pillow'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
CKEDITOR_STORAGE_BACKEND = 'django.core.files.storage.FileSystemStorage'
customColorPalette = [
    {
        'color': 'hsl(4, 90%, 58%)',
        'label': 'Red'
    },
    {
        'color': 'hsl(340, 82%, 52%)',
        'label': 'Pink'
    },
    {
        'color': 'hsl(291, 64%, 42%)',
        'label': 'Purple'
    },
    {
        'color': 'hsl(262, 52%, 47%)',
        'label': 'Deep Purple'
    },
    {
        'color': 'hsl(231, 48%, 48%)',
        'label': 'Indigo'
    },
    {
        'color': 'hsl(207, 90%, 54%)',
        'label': 'Blue'
    },
]

CKEDITOR_5_ALLOW_ALL_FILE_TYPES = True
CKEDITOR_5_UPLOAD_FILE_TYPES = ['jpeg', 'pdf', 'png', 'jpg']  # optional
CKEDITOR_5_CUSTOM_CSS = 'static/css/custom_ckeditor.css'  # optional
# CKEDITOR_5_FILE_STORAGE = "apps.storage.CustomStorage"  # optional
CKEDITOR_5_CONFIGS = {
    'default': {
        # 'toolbar': ['heading', '|', 'bold', 'italic', 'link',
        #             'bulletedList', 'numberedList', 'blockQuote', 'imageUpload', ],
        'toolbar': 'full',
        'extraPlugins': 'divarea',  # Make sure the divarea plugin is enabled
        'contentsCss': ['/static/css/custom_ckeditor.css'],
    },
    'extends': {
        'blockToolbar': [
            'paragraph', 'heading1', 'heading2', 'heading3',
            '|',
            'bulletedList', 'numberedList',
            '|',
            'blockQuote',
        ],
        'toolbar': ['heading', '|', 'outdent', 'indent', '|', 'bold', 'italic', 'link', 'underline', 'strikethrough',
                    'code', 'subscript', 'superscript', 'highlight', '|', 'codeBlock', 'sourceEditing', 'insertImage',
                    'bulletedList', 'numberedList', 'todoList', '|', 'blockQuote', 'imageUpload', '|',
                    'fontSize', 'fontFamily', 'fontColor', 'fontBackgroundColor', 'mediaEmbed', 'removeFormat',
                    'insertTable', ],
        'image': {
            'toolbar': ['imageTextAlternative', '|', 'imageStyle:alignLeft',
                        'imageStyle:alignRight', 'imageStyle:alignCenter', 'imageStyle:side', '|'],
            'styles': [
                'full',
                'side',
                'alignLeft',
                'alignRight',
                'alignCenter',
            ]

        },
        'table': {
            'contentToolbar': ['tableColumn', 'tableRow', 'mergeTableCells',
                               'tableProperties', 'tableCellProperties'],
            'tableProperties': {
                'borderColors': customColorPalette,
                'backgroundColors': customColorPalette
            },
            'tableCellProperties': {
                'borderColors': customColorPalette,
                'backgroundColors': customColorPalette
            }
        },
        'heading': {
            'options': [
                {'model': 'paragraph', 'title': 'Paragraph', 'class': 'ck-heading_paragraph'},
                {'model': 'heading1', 'view': 'h1', 'title': 'Heading 1', 'class': 'ck-heading_heading1'},
                {'model': 'heading2', 'view': 'h2', 'title': 'Heading 2', 'class': 'ck-heading_heading2'},
                {'model': 'heading3', 'view': 'h3', 'title': 'Heading 3', 'class': 'ck-heading_heading3'}
            ]
        }
    },
    'list': {
        'properties': {
            'styles': 'true',
            'startIndex': 'true',
            'reversed': 'true',
        }
    },

    }

# settings.py

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'extraPlugins': 'divarea',  # Make sure the divarea plugin is enabled
        'contentsCss': ['/static/css/custom_ckeditor.css'],
    },
}

JAZZMIN_SETTINGS = {
    "site_title": "Django Rest API",
    "site_header": "Django Rest API",
    "site_brand": "Django Rest API",
    "welcome_sign": "Django Rest API Admin",
    "show_sidebar": True,
    "navigation_expanded": True,
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
    },
    "copyright": "Django Rest API",
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",
    "related_modal_active": False,
    "custom_js": None,
    "use_google_fonts_cdn": True,
    "changeform_format": "horizontal_tabs",
    "changeform_format_overrides": {
        "auth.user": "collapsible",
        "auth.group": "vertical_tabs",
    },
    "site_logo_classes": "img-circle",
}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": True,
    "brand_small_text": False,
    "brand_colour": "navbar-navy",
    "accent": "accent-primary",
    "navbar": "navbar-navy navbar-dark",
    "no_navbar_border": False,
    "navbar_fixed": False,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": True,
    "sidebar": "sidebar-dark-navy",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": True,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "theme": "minty",
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-outline-primary",
        "secondary": "btn-outline-secondary",
        "info": "btn-outline-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success",
    },
    "actions_sticky_top": False,
}
