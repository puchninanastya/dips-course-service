from rest_framework import serializers

from .models import Course

class CourseSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='pk', read_only=True)
    class Meta:
        model = Course
        fields = '__all__'
