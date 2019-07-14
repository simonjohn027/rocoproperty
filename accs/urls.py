from django.urls import re_path,path
from .views import (
        RegisterView,
        AccountEmailActivateView,
        UserDetailUpdateView,
        LoginView,logout_view
        )

app_name = 'accs'

urlpatterns = [
    path('reg/', RegisterView.as_view(), name='registration'),
    path('login/', LoginView.as_view(),name = 'login'),
    path('logout/',logout_view,name = 'logout'),
    path('details/', UserDetailUpdateView.as_view(), name='user-update'),
    re_path(r'^email/confirm/(?P<key>[0-9A-Za-z]+)/$',
            AccountEmailActivateView.as_view(),
            name='email-activate'),
    re_path(r'^email/resend-activation/$',
            AccountEmailActivateView.as_view(),
            name='resend-activation'),
]
