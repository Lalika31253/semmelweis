# semmelweis_project/settings.py
# Only the additions / changes from the default are shown.

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-your-secret-key-here'

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

ROOT_URLCONF = 'semmelweis_project.urls'
WSGI_APPLICATION = 'semmelweis_project.wsgi.application'

# ── Installed apps ────────────────────────────────────────────────────────────
# Add 'analysis' so Django discovers models, admin, and static files inside it.
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'analysis',   # ← register the analysis app
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# ── Templates ─────────────────────────────────────────────────────────────────
# DIRS tells Django to look in the project-level templates/ folder first.
# APP_DIRS: True also allows templates inside each app's own templates/ folder.
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],  # ← critical: point at project templates/
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

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# ── Static files ──────────────────────────────────────────────────────────────
# STATIC_URL is the URL prefix for serving static files.
# STATICFILES_DIRS tells Django where to look for additional static files
# that are NOT inside an app's static/ sub-folder.
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

# ── Media files ───────────────────────────────────────────────────────────────
# MEDIA_URL / MEDIA_ROOT handle user-uploaded content (the portrait photo and
# any files uploaded via the CSV import form).
MEDIA_URL  = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# ── Primary key ───────────────────────────────────────────────────────────────
# BigAutoField uses a 64-bit integer for primary keys — good practice for
# tables that could grow large.
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'