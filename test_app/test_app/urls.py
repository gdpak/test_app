from django.conf            import settings
from django.contrib         import admin
from django.conf.urls       import url
from django.conf.urls       import include
from django.conf.urls       import patterns
from social.apps.django_app import urls as social_urls

from user_management.views import Index
from user_management.views import Login
from user_management.views import Logout


urlpatterns = [
    url(''        , include(social_urls, namespace='social')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$'       , Index .as_view(), name='index' ),
    url(r'^login/$' , Login .as_view(), name='login' ),
    url(r'^logout/$', Logout.as_view(), name='logout'),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns(
        '',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
