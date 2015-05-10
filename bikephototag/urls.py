from django.conf.urls import patterns, include, url
from bikephototag.apps.phototag.views import Index, LocationDetail,\
     NewLocationEvent, AddNewLocation, Login
from django.conf.urls.static import static
from django.conf import settings


# import autocomplete_light
# autocomplete_light.autodiscover()

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', Index.as_view()),
    url(r'^l/$', Login.as_view()),
    url(r'^(?P<location_id>\d+)/next/$', NewLocationEvent.as_view()),
    url(r'^(?P<location_id>\d+)/new/$', AddNewLocation.as_view()),
    url(r'^(?P<location_id>\d+)/$', LocationDetail.as_view()),

    url(r'^admin/', include(admin.site.urls)),
    # url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
