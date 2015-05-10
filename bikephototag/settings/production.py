from bikephototag.settings.base import *
import os

DEBUG = True
TEMPLATE_DEBUG = False

INSTALLED_APPS.append('raven.contrib.django.raven_compat')

DATABASES['default'] = dj_database_url.config()
DEBUG_TOOLBAR_PATCH_SETTINGS = False
RAVEN_CONFIG = {
    'dsn': 'https://7106e6be67f7403c8ada95955523298b:9f5c8b44b5fc47b68320b3facfdaf544@s.peakdata.net/4',
}
os.environ['wsgi.url_scheme'] = 'https'
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '172.17.42.1:11211',
        'KEY_PREFIX': os.environ['MEMCACHE_PREFIX'],
    }
}
