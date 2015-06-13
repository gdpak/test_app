from django.contrib   import admin
from django.conf.urls import url
from django.conf.urls import include

from user_management.views import index
from user_management.views import logout

urlpatterns = [
    url(r'^admin/'  , include(admin.site.urls)),
    url(r'^$'       , index),
    url(''          , include('social.apps.django_app.urls', namespace='social')),
    url(r'^logout/$', logout),
]
