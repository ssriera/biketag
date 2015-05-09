from django.contrib import admin
from bikephototag.apps.phototag import models

admin.site.register(models.Location)
admin.site.register(models.PhotoEvent)
