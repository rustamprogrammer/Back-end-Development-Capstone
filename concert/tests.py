from unittest.mock import patch, Mock
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Concert, ConcertAttending


class BandWebsiteTests(TestCase):
    def test_home_and_protected_concerts(self):
        self.assertEqual(self.client.get('/').status_code, 200)
        self.assertEqual(self.client.get('/concerts/').status_code, 302)

    def test_registration_login_and_logout(self):
        response = self.client.post('/signup/', {'username': 'listener',
            'password1': 'BandTest2026!', 'password2': 'BandTest2026!'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.client.get('/concerts/').status_code, 200)
        self.client.get('/logout/')
        self.assertEqual(self.client.get('/concerts/').status_code, 302)
        response = self.client.post('/login/', {'username': 'listener', 'password': 'BandTest2026!'})
        self.assertEqual(response.status_code, 302)

    @patch('concert.views.req.get')
    def test_microservice_data_reaches_templates(self, get):
        get.return_value = Mock(json=lambda: [{'id': 1, 'title': 'Test melody', 'lyrics': 'Hello'}])
        self.assertContains(self.client.get('/songs/'), 'Test melody')
        get.return_value = Mock(json=lambda: [{'id': 1, 'pic_url': '/static/images/img.jpeg', 'event_city': 'Astana'}])
        self.assertContains(self.client.get('/photos/'), 'Astana')

    def test_attendance_is_scoped_to_signed_in_user(self):
        user = User.objects.create_user('listener', password='BandTest2026!')
        concert = Concert.objects.create(concert_name='Live', duration=2, city='Astana', date='2026-12-01')
        self.client.force_login(user)
        response = self.client.post('/concert_attendee/', {'concert_id': concert.id, 'attendee_choice': 'Attending'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(ConcertAttending.objects.get(user=user, concert=concert).attending, 'Attending')
