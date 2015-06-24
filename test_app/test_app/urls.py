from django.conf            import settings
from django.contrib         import admin
from django.conf.urls       import url
from django.conf.urls       import include
from django.conf.urls       import patterns
from social.apps.django_app import urls as social_urls

from user_management.views          import IndexView
from user_management.views.auth     import LoginView
from user_management.views.auth     import LogoutView
from user_management.views.accounts import ListAccountsView
from user_management.views.accounts import CreateAccountView
from user_management.views.accounts import DeleteAccountView
from user_management.views.accounts import UpdateAccountView
from user_management.views.accounts import DeleteAccountsView
from user_management.views.rest_api import IBANGeneratorApiView
from user_management.views.rest_api import DeleteAccountsApiView


urlpatterns = [
    url(''           , include(social_urls, namespace='social')),
    url(r'^admin/'   , include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^$'       , IndexView .as_view(), name='index' ),
    url(r'^login/$' , LoginView .as_view(), name='login' ),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),

    url(r'^list_accounts/$'                        , ListAccountsView  .as_view(), name='list_accounts'  ),
    url(r'^create_account/$'                       , CreateAccountView .as_view(), name='create_account' ),
    url(r'^update_account/(?P<account_id>[0-9]+)/$', UpdateAccountView .as_view(), name='update_account' ),
    url(r'^delete_account/(?P<account_id>[0-9]+)/$', DeleteAccountView .as_view(), name='delete_account' ),
    url(r'^delete_accounts/((?P<accounts>.+)/)*$'  , DeleteAccountsView.as_view(), name='delete_accounts'),

    url(r'^api/generate_iban/$'  , IBANGeneratorApiView .as_view(), name='generate_iban_api'  ),
    url(r'^api/delete_accounts/$', DeleteAccountsApiView.as_view(), name='delete_accounts_api'),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns(
        '',
        url(r'^__debug__/', include(debug_toolbar.urls)))
