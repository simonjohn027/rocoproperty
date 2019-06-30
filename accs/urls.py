from django.conf.urls import re_path
from .views import (
        AccountHomeView,
        AccountEmailActivateView,
        UserDetailUpdateView
        )

app_name = 'accs'

urlpatterns = [

    re_path(r'^$', AccountHomeView.as_view(), name='login'),
    re_path(r'^details/$', UserDetailUpdateView.as_view(), name='user-update'),
    re_path(r'^email/confirm/(?P<key>[0-9A-Za-z]+)/$',
            AccountEmailActivateView.as_view(),
            name='email-activate'),
    re_path(r'^email/resend-activation/$',
            AccountEmailActivateView.as_view(),
            name='resend-activation'),
]
