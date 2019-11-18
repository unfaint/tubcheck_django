from PIL import Image
import os
from django.test import TestCase, Client
from django.urls import resolve
from django.conf import settings
from oneimage import views


class HomePageTest(TestCase):

    def test_url_resolves_to_view_function(self):
        found = resolve('/')
        self.assertEqual(found.func, views.home_page)

    def test_home_page_returns_html(self):
        c = Client()

        response = c.get('/')

        self.assertContains(response, 'html')


class UploadPageTest(TestCase):

    def test_redirect_on_post(self):
        c = Client()
        with open(os.path.join(settings.BASE_DIR, 'xray.jpg'), 'rb') as f:
            image = Image.open(f)

        response = c.post(
            '/oneimage/check',
            data={'image': image}
        )

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/oneimage/results')
