from bikephototag.settings.base import *

DATABASES['default']['NAME'] = 'bikephototag_development'
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'bikephototag'
    }
}

COMPRESS_ENABLED = True
