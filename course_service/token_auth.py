from django.utils import timezone
from rest_framework import authentication, exceptions
from .models import Token

class AppTokenAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        token = str(request.META.get('HTTP_AUTHORIZATION')).split()[-1]
        if token == 'None':
            raise exceptions.AuthenticationFailed('No token')
        try:
            tok = Token.objects.get(token=token)
        except Token.DoesNotExist:
            raise exceptions.AuthenticationFailed('No app with such token')

        if tok.expires < timezone.now():
            raise exceptions.AuthenticationFailed('Token expired')
        return (None, None)

    def authenticate_header(self, request):
        return 'AppTokenAuthentication'
