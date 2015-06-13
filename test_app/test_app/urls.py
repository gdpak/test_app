from django.contrib   import admin
from django.conf.urls import url
from django.conf.urls import include

from user_management.views import index
from user_management.views import login
from user_management.views import logout
from user_management.views import account_login

urlpatterns = [
    url(''            , include('social.apps.django_app.urls', namespace='social')),
    url(r'^$'         , index ),
    url(r'^admin/'    , include(admin.site.urls)),
    url(r'^login/$'   , login ),
    url(r'^logout/$'  , logout),
    url(r'^auth_login', account_login, name='auth_login'),
]
