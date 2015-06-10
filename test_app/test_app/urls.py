from django.contrib   import admin
from django.conf.urls import url
from django.conf.urls import include

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(''        , include('social.apps.django_app.urls', namespace='social')),
]
