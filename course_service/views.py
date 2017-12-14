from django.shortcuts import render

from rest_framework import viewsets, mixins
from rest_framework import status

from .serializers import CourseSerializer
from .models import Course

#TODO: Create tests for views
#TODO: Create pagination

class CourseViewSet(mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     viewsets.GenericViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
