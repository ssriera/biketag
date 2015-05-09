from django.conf.urls import patterns, url


from bikephototag.apps.site import views

urlpatterns = patterns('',
    # url(r'^$', views.HomePage.as_view(), name='home'),
    # url(r'^accounts/login/(?P<secret_code>[0-9\-_=\w]+)/$',
    #     views.SecretCodeLogin.as_view()
    #     ),
    # url(r'^accounts/login/$',
    #     views.EmailLogin.as_view()
    #     ),
    # url(r'^support/$',
    #     views.SupportPage.as_view()
    #     ),
)
