from django.utils import timezone

from rest_framework import viewsets, mixins
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response

from .serializers import CourseSerializer
from .models import Course, Token
from .token_auth import AppTokenAuthentication

import binascii
import os

class TokenView(APIView):
    def get(self, request):
        clientId = request.query_params.get('clientId')
        clientSecret = request.query_params.get('clientSecret')
        try:
            tok = Token.objects.get(client_id=clientId, client_secret=clientSecret)
        except Token.DoesNotExist:
            return Response(status=status.HTTP_403_FORBIDDEN)
        new_token = binascii.hexlify(os.urandom(15)).decode('ascii')
        tok.token = new_token
        tok.expires = timezone.now() + timezone.timedelta(minutes=1)
        tok.save()
        return Response({'token': new_token})

class CourseViewSet(mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    authentication_classes = (AppTokenAuthentication, )
