
from django.urls import path
from . import  views

app_name = 'main'
urlpatterns = [
    path("", views.index, name = "index"),
    path("props",views.propertyList, name = "list"),
    path("prop",views.property, name = "property"),
    path('search', views.PropertySearch.as_view(), name='search'),
    path("owner",views.owners, name = "owner"),
    path("contact",views.Contact.as_view(), name = "contact")
]
