from django.conf            import settings
from django.contrib         import admin
from django.conf.urls       import url
from django.conf.urls       import include
from django.conf.urls       import patterns
from social.apps.django_app import urls as social_urls

from user_management.views          import Index
from user_management.views.auth     import Login
from user_management.views.auth     import Logout
from user_management.views.accounts import ListAccounts
from user_management.views.accounts import CreateAccount
from user_management.views.accounts import DeleteAccount
from user_management.views.accounts import UpdateAccount
from user_management.views.rest_api import IBANGenerator


urlpatterns = [
    url(''           , include(social_urls, namespace='social')),
    url(r'^admin/'   , include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^$'       , Index .as_view(), name='index' ),
    url(r'^login/$' , Login .as_view(), name='login' ),
    url(r'^logout/$', Logout.as_view(), name='logout'),

    url(r'^list_accounts/$'                        , ListAccounts .as_view(), name='list_accounts' ),
    url(r'^create_account/$'                       , CreateAccount.as_view(), name='create_account'),
    url(r'^update_account/(?P<account_id>[0-9]+)/$', UpdateAccount.as_view(), name='update_account'),
    url(r'^delete_account/(?P<account_id>[0-9]+)/$', DeleteAccount.as_view(), name='delete_account'),

    url(r'^api/generate_iban/$', IBANGenerator.as_view(), name='generate_iban')
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns(
        '',
        url(r'^__debug__/', include(debug_toolbar.urls)))
