
from local_settings import *
import site
site.addsitedir('/home/faunris/modules')
site.addsitedir('/home/faunris/venv/lib/python2.6/ste-packeges')
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Alan', 'Faunris@gmail.com'),
)

MANAGERS = ADMINS

TIME_ZONE = 'Asia/Yekaterinburg'
LANGUAGE_CODE = 'ru-ru'
SITE_ID = 1
USE_I18N = True
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

MEDIA_ROOT = '%s/public/media/' % PROJECT_DIR
MEDIA_URL = '/media/'

STATIC_ROOT = ''
STATIC_URL = 'http://dl.dropbox.com/u/15834380/static/'

STATICFILES_DIRS = (

)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)



TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'pages.middleware.PageMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = ("django.contrib.auth.context_processors.auth",
                               "django.core.context_processors.debug",
                               "django.core.context_processors.i18n",
                               "django.core.context_processors.media",
                               "django.core.context_processors.static",
                               "django.core.context_processors.tz",
                               "django.contrib.messages.context_processors.messages",
                               "django.core.context_processors.request")


ROOT_URLCONF = 'urls'#'%s.urls' % PROJECT_NAME

WSGI_APPLICATION = '%s.wsgi.application' % PROJECT_NAME

TEMPLATE_DIRS = (
    '%s/templates' % PROJECT_DIR,
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)
ACCOUNT_ACTIVATION_DAYS = 2
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'treeadmin',
    'mptt',
    'website',
    'south',
    'tinymce',
    'grappelli',
    'filebrowser',
    'pages',
    's_test',
    'accounts',
    'registration',
    'django.contrib.admin',
    'django.contrib.admindocs',

)
ADMIN_MEDIA_PREFIX = STATIC_URL + "grappelli/"
AUTH_PROFILE_MODULE = 'accounts.UserProfile'
LOGIN_REDIRECT_URL = 'accounts/profile/'
GRAPPELLI_ADMIN_TITLE = PROJECT_TITLE

TINYMCE_DEFAULT_CONFIG = {
    'plugins' : "safari,pagebreak,style,layer,table,save,advhr,advimage,advlink,emotions,iespell,inlinepopups,insertdatetime,preview,media,searchreplace,print,contextmenu,paste,directionality,fullscreen,noneditable,visualchars,nonbreaking,xhtmlxtras,template",
    'theme': "advanced",
    'theme_advanced_buttons1' : "bold,italic,underline,strikethrough,|,justifyleft,justifycenter,justifyright,|,styleselect,formatselect",
    'theme_advanced_buttons2' : "cut,copy,paste,pasteword,|,bullist,numlist,|,outdent,indent,blockquote,|,undo,redo,|,link,unlink,anchor,image,cleanup,code,|,forecolor,backcolor",
    'theme_advanced_buttons3' : "tablecontrols,|,hr,removeformat,visualaid,|,sub,sup,|,charmap,iespell,media,advhr,|,fullscreen",
    'theme_advanced_toolbar_location' : "top",
    'theme_advanced_toolbar_align' : "left",
    'theme_advanced_statusbar_location' : "bottom",
    'theme_advanced_resizing' : "true",
    }

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

