from django.urls import path
from serializerapp import views
from rest_framework.urlpatterns import format_suffix_patterns


app_name = 'serializer'
urlpatterns = [
    path("",views.api_root, name = 'root'),
    path('properties/', views.PropertiesList.as_view(), name = 'properties'),
    path('property/<slug:slug>/', views.PropertyDetail.as_view(), name = 'property'),
    path('users/', views.UserList.as_view(),name = 'users'),
    path('user/<int:pk>/', views.UserDetail.as_view(), name ='user'),
]

urlpatterns = format_suffix_patterns(urlpatterns)