from django.test import TestCase, Client
from django.urls import resolve
from oneimage import views


class HomePageTest(TestCase):

    def test_url_resolves_to_view_function(self):
        found = resolve('/')
        self.assertEqual(found.func, views.home_page)

    def test_home_page_returns_html(self):
        c = Client()

        response = c.get('/')

        self.assertContains(response, 'html')
