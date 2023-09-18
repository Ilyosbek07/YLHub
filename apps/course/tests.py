from rest_framework import status

from apps.course.models import Course, Category, UserCourse, Lesson
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
            name='cat 1'
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
            duration_day=15,
            expired_date='2023-09-21',
            score=45,
            main_image=self.uploaded_file
        )
        self.user_course = UserCourse.objects.create(
            user=self.user,
            course=self.course
        )
        self.course_lesson = Lesson.objects.create(
            course=self.course,
            title='lesson_1',
            description='desc',
            type='video',
            order=1
        )

    def test_category_list(self):
        response = self.client.get(reverse('category_list'))
        self.assertEqual(response.status_code, 200)
        print(response.data)
        self.assertEqual(response.data["results"][0]["name"], 'cat 1')

    def test_course_list(self):
        response = self.client.get(reverse('course_list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["results"][0]["title"], 'test_title')

    def test_course_detail(self):
        response = self.client.get(reverse('course_detail', kwargs={"pk": self.profile.id}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["title"], 'test_title')

    # def test_user_submit_to_course(self):
    #     data = {
    #         'course': self.course.id
    #     }
    #     response = self.client.post(reverse('user_course_create_list'), data=data,format='json')
    #     self.assertEqual(response, status.HTTP_201_CREATED)

    def test_user_course_list(self):
        response = self.client.get(reverse('user_course_list', kwargs={"pk": self.user.id}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["results"][0]["course"]["title"], 'test_title')

    def test_user_course_detail(self):
        response = self.client.get(reverse('user_course_detail', kwargs={"pk": self.user_course.id}))
        self.assertEqual(response.status_code, 200)

    def test_lesson_detail(self):
        response = self.client.get(reverse('lesson_detail', kwargs={"pk": self.course_lesson.id}))
        self.assertEqual(response.status_code, 200)
