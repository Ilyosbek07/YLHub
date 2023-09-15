from apps.course.models import Course, Category
from apps.users.models import User
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from apps.users.models import Profile


class CourseTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            username='Test User',
            password='Test Password'
        )
        self.profile = Profile.objects.create(
            user=self.user,
            full_name='test',
            position='test',
            JShShIR='test',
            study_center='test',
            passport_series='test',
            nationality='test',
            degree='test',
            score=123,
        )

        self.category = Category.objects.create(
            name='asdds',
            is_optional=False
        )
        self.uploaded_file = SimpleUploadedFile(
            "test_file.png",
            b"Test content for the file",
            content_type="text/plain"
        )
        self.course = Course.objects.create(
            category=self.category,
            title='test_title',
            desc='test_desc',
            duration_time=15,
            score=45,
            main_image=self.uploaded_file
        )

    def test_course_list(self):
        response = self.client.get(reverse('course_list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["results"][0]["title"], 'test_title')

    def test_course_detail(self):
        response = self.client.get(reverse('course_detail', kwargs={"pk": self.profile.id}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["results"][0]["title"], 'test_title')
