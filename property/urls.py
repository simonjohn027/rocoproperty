
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('main.urls')),
    path("accs/", include("accs.urls")),
    path('api/',include('serializerapp.urls')),
    path('customer/',include('customer.urls')),

    path('login/', auth_views.auth_login, name='login'),
    path('oauth/', include('social_django.urls', namespace='social')),

    path('api-auth/', include('rest_framework.urls')),
]

handler404 = 'main.views.error_404_view'