from django.utils import timezone
from rest_framework import permissions
from .models import Token

class HasValidClientToken(permissions.BasePermission):
    def has_permission(self, request, view):
        token = str(request.META.get('HTTP_AUTHORIZATION')).split()[-1]
        if self.is_token_valid(token):
            return True
        return False

    def is_token_valid(self, token):
        try:
            tok = Token.objects.get(token=token)
        except Token.DoesNotExist:
            return False
        if tok.expires < timezone.now():
            return False
        return True
