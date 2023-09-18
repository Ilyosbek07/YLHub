from rest_framework import status

from apps.users.models import User
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase, APIClient

from apps.users.models import Profile


class ProfileTestCase(APITestCase):
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

    def test_user_detail(self):
        self.client.force_login(self.profile.user)
        response = self.client.get(reverse('profile_detail', kwargs={"pk": self.profile.id}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["full_name"], 'test')


class RegistrationAPITestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.register_url = reverse('register')

    def test_user_registration(self):
        user_data = {
            'username': 'testuser',
            'password': 'testpassword',
        }

        response = self.client.post(self.register_url, user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)

        self.assertIn('access', response.data['token'])
        self.assertIn('refresh', response.data['token'])
