from django.test import TestCase
from django.core.urlresolvers import resolve

from app.views import home


class HomePageTest(TestCase):

  def test_root_url_resolves_to_the_home_page(self):

    # Make sure we're calling the home view function
    found = resolve('/')
    self.assertEqual(found.func, home)


  def test_home_page_renders_home_template(self):

    # Make sure we're rendering the home template
    response = self.client.get('/')
    self.assertTemplateUsed(response, 'home.html')
