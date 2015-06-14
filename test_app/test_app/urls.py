from django.contrib         import admin
from django.conf.urls       import url
from django.conf.urls       import include
from social.apps.django_app import urls as social_urls

from user_management.views import index
from user_management.views import Login
from user_management.views import Logout


urlpatterns = [
    url(''        , include(social_urls, namespace='social')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$'       , index ),
    url(r'^login/$' , Login.as_view(), name='login'),
    url(r'^logout/$', Logout.as_view(), name='logout'),
]
