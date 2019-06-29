
from django.urls import path
from . import  views

urlpatterns = [
    path("", views.index, name = "index"),
    path("props",views.propertyList, name = "list"),
    path("prop",views.property, name = "property"),
    path("contact",views.contact, name = "contact")
]
