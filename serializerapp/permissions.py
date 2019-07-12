from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
        Custom permission to only allow owners of an object to edit it.
        """

    def has_object_permission(self, request, view, obj):
        #Read permissions are allowed to any request,
        #Hence GET, HEAD and OPTIONS requests

        if request.methon in permissions.SAFE_METHODS:
            return True

        #Write permission are only allowed to the owner of propety
        return obj.owner == request.user
