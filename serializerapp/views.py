from main.models import Property
from accs.models import User
from .serializer import PropertySerializer,UserSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
from django.contrib.auth.decorators import login_required


@login_required(login_url='/accs/login/')
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('serializer:users', request=request, format=format),
        'properties': reverse('serializer:properties', request=request, format=format)
    })


class PropertiesList(generics.ListCreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

    perpermission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PropertyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)


class UserList(generics.ListAPIView):
    queryset =  User.objects.all()
    serializer_class =  UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset =  User.objects.all()
    serializer_class = UserSerializer



