from django.conf.urls import patterns, include, url
from bikephototag.apps.phototag.views import Index

# import autocomplete_light
# autocomplete_light.autodiscover()

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('bikephototag.apps.site.urls', namespace='site')),
    url(r'^$', Index.as_view()),
    # url(r'^', include('jmtwear.apps.gearlist.urls', namespace='gearlist')),
    # url(r'^autocomplete/', include('autocomplete_light.urls')),
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
)
