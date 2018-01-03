from django.test import TestCase

from course_service.models import Course

class ModelTestCase(TestCase):
    """This class defines the test suite for the Course model."""

    def setUp(self):
        self.newCourse1 = Course.objects.create(name='course1',
            description='desc1')

    def test_model_get_course(self):
        """Test the course model can get course."""
        course1 = Course.objects.get(self.newCourse1.pk)
        self.assertEqual(course1.name, 'course1')
        self.assertEqual(course1.description, 'desc1')
