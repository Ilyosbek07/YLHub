from apps.users.models import User
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

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
