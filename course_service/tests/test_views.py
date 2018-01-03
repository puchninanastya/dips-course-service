from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse

from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.test import APIRequestFactory

from course_service.models import Course
from course_service.serializers import CourseSerializer
from course_service.views import CourseViewSet

class GetAllCoursesTestCase(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = APIRequestFactory()

        self.newCourse1 = Course.objects.create(name='course1',
            description='desc1', price=1000)
        self.newCourse2 = Course.objects.create(name='course2',
            description='desc2', price=2000)
        self.newCourse3 = Course.objects.create(name='course3',
            description='desc3', price=3000)

    def test_get_all_courses(self):
        """Test the api get courses."""
        # Setup.
        url = "/courses/"
        request = self.factory.get(url)
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        # Run.
        course_list = CourseViewSet.as_view({'get': 'list'})
        response = course_list(request)
        # Check.
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'], serializer.data)

class GetSingleCourseTestCase(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = APIRequestFactory()

        self.newCourse1 = Course.objects.create(name='course1',
            description='desc1', price=1000)

        self.invalid_pk = 2

    def test_get_valid_single_course(self):
        """Test the api get valid single course."""
        # Setup.
        url = "/courses/" + str(self.newCourse1.pk)
        request = self.factory.get(url)
        serializer = CourseSerializer(self.newCourse1)
        # Run.
        course_detail = CourseViewSet.as_view({'get': 'retrieve'})
        response = course_detail(request, pk=self.newCourse1.pk)
        # Check.
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_invalid_single_user(self):
        """Test the api get invalid single course."""
        # Setup.
        url = "/courses/" + str(self.invalid_pk)
        request = self.factory.get(url)
        # Run.
        course_detail = CourseViewSet.as_view({'get': 'retrieve'})
        response = course_detail(request, pk=self.invalid_pk)
        # Check.
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class CreateNewCourseTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = APIRequestFactory()

        self.valid_payload = {
            "name": "Диетология",
            "description": "Описание курса диетологии.",
            "start_date": "2018-01-22",
            "end_date": "2018-02-22",
            "price": 7000
        }

        self.invalid_payload = {
            "name": "",
            "description": "Описание курса .",
            "start_date": "2018-01-22",
            "end_date": "2018-02-22",
            "price": 7000
        }

    def test_create_valid_single_course(self):
        """Test the api valid insert new course."""
        # Setup.
        url = "/courses/"
        request = self.factory.post(url, self.valid_payload, format='json')
        # Run.
        course_list = CourseViewSet.as_view({'post': 'create'})
        response = course_list(request)
        # Check.
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_single_user(self):
        """Test the api invalid insert new course."""
        # Setup.
        url = "/courses/"
        request = self.factory.post(url, self.invalid_payload, format='json')
        # Run.
        course_list = CourseViewSet.as_view({'post': 'create'})
        response = course_list(request)
        # Check.
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class DeleteSingleCourseTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = APIRequestFactory()

        self.newCourse1 = Course.objects.create(name='course1',
            description='desc1', price=1000)

        self.invalid_pk = 2

    def test_delete_valid_single_course(self):
        """Test the api valid delete new course."""
        # Setup.
        url = "/courses/" + str(self.newCourse1.pk)
        request = self.factory.delete(url)
        # Run.
        course_detail = CourseViewSet.as_view({'delete': 'destroy'})
        response = course_detail(request, pk=self.newCourse1.pk)
        # Check.
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_valid_single_course(self):
        """Test the api valid delete new course."""
        # Setup.
        url = "/courses/" + str(self.invalid_pk)
        request = self.factory.delete(url)
        # Run.
        course_detail = CourseViewSet.as_view({'delete': 'destroy'})
        response = course_detail(request, pk=self.invalid_pk)
        # Check.
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
