from django.test import TestCase
from django.core.urlresolvers import resolve

from app.views import home


class HomePageTest(TestCase):

  def test_root_url_resolves_to_the_home_function(self):

    # Make sure we're calling the home view function
    found = resolve('/')
    self.assertEqual(found.func, home)


  def test_home_renders_home_template(self):

    # Make sure we're rendering the home template
    response = self.client.get('/')
    self.assertTemplateUsed(response, 'home.html')


  def test_home_returns_google_api_key_context_var(self):

    response = self.client.get('/')
    self.assertIn('GOOGLE_API_KEY', response.context)
