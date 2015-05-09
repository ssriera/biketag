from bikephototag.settings.base import *
import os

DEBUG = False
TEMPLATE_DEBUG = False

INSTALLED_APPS.append('raven.contrib.django.raven_compat')

# DATABASES['default'] = {
#         'ENGINE':'django.db.backends.postgresql_psycopg2',
#         'NAME': 'jmtwear_production',
#         'USER': 'jmtwear_123',
#         'PASSWORD': '12jlkaajfjjjjjj8f8f8AVVVa1',
#         'HOST': '172.17.42.1',
#         'PORT': '5432',
#     }
DATABASES['default'] = dj_database_url.config()
DEBUG_TOOLBAR_PATCH_SETTINGS = False
# RAVEN_CONFIG = {
#     'dsn':
#         'https://@s.peakdata.net/2',
# }
os.environ['wsgi.url_scheme'] = 'https'
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '172.17.42.1:11211',
        'KEY_PREFIX': os.environ['MEMCACHE_PREFIX'],
    }
}
