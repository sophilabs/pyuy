import os
gettext = lambda s: s
PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
PROJECT_ROOT = os.path.join(PROJECT_PATH, '..')

def rel(*x):
    return os.path.join(PROJECT_ROOT, *x)

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'pyuy',                      # Or path to database file if using sqlite3.
        'USER': 'sl',                      # Not used with sqlite3.
        'PASSWORD': 'sl',                  # Not used with sqlite3.
        'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'


STATIC_ROOT = rel('collectedstatic')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    rel('static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'zq($m9-l453vuha7wn(0p_xq38xb&amp;6a15^=3ix--#wu(zq)_u5'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'cms.middleware.multilingual.MultilingualURLMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cmsplugin_blog.middleware.MultilingualBlogEntriesMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'pyuy.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'pyuy.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH, 'templates'),

)
CMS_TEMPLATES = (
    ('cmsplugin_blog/base_extended.html', 'Base'),
    ('cmsplugin_blog/base_pycon_extended.html', 'Base PyCon'),
    ('cmsplugin_blog/profile_extended.html', 'Profile'),
    ('cmsplugin_blog/cmsplugin_blog_base.html','cmsplugin_blog'),
    ('cmsplugin_blog/entry_detail.html','cmsplugin_blog_detail'),
)
CMS_LANGUAJES = (
    ('en', gettext('English')),
    ('es', gettext('Spanish')),
)

LANGUAGES = (
    ('en', gettext('English')),
    ('es', gettext('Spanish')),
)
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'cms.context_processors.media',
    'sekizai.context_processors.sekizai',
    'django.contrib.messages.context_processors.messages',
    'pyuy.context_processors.background',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',

    'account',

    'symposion.conference',
    'symposion.speakers',
    'symposion.proposals',
    'symposion.review',
    'symposion.sponsors_pro',
    'symposion.schedule',

    'bootstrap',
    'pyuy',
    'pycon',

    'cms',
    'mptt',
    'menus',
    'south',
    'sekizai',
    'cms.plugins.file',
    'cms.plugins.flash',
    'cms.plugins.googlemap',
    'cms.plugins.link',
    'cms.plugins.picture',
    'cms.plugins.teaser',
    'cms.plugins.text',
    'cms.plugins.video',
    'cms.plugins.twitter',

    'cmsplugin_blog',
    'djangocms_utils',
    'simple_translation',
    'tagging',
    'django.contrib.staticfiles',
    'missing',
)

ACCEPTING_PROPOSALS = True
MARKITUP_AUTO_PREVIEW = True
MARKITUP_SET = "markitup/sets/markdown-custom"
MARKITUP_SKIN = "markitup/skins/simple"
MARKITUP_FILTER = ["markdown.markdown", {}]
MARKITUP_MEDIA_URL = STATIC_URL

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
JQUERY_JS = 'https://ajax.googleapis.com/ajax/libs/jquery/1.4.4/jquery.min.js'
JQUERY_UI_JS = 'https://ajax.googleapis.com/ajax/libs/jqueryui/1.8.12/jquery-ui.min.js'
JQUERY_UI_CSS = 'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.12/themes/smoothness/jquery-ui.css'
CMSPLUGIN_BLOG_PLACEHOLDERS = ('text',)