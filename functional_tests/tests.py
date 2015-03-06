import sys

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from django.test import LiveServerTestCase


class NewVisitorTest(LiveServerTestCase):

  def setUp(self):
    self.browser = webdriver.Chrome()
    self.browser.implicitly_wait(3)

  def tearDown(self):
    self.browser.quit()


  ### Test Methods ###
  def test_can_see_map_a_filter_by_search_text(self):
    # The user goes to the web site
    self.browser.get(self.live_server_url)

    # The user sees a search box at the top of the page
    searchbox = self.browser.find_element_by_id('id_search_input')

    # The user then also sees a map below the search box
    map_area = self.browser.find_element_by_id('id_map')

    # The user decides to filter for the movie "180"
    searchbox.send_keys('180')

    # The user sees an autocomplete selection of results
    autocomplete_list = self.browser.find_element_by_class_name('ui-autocomplete')
    autocomplete_tags = autocomplete_list.find_elements_by_tag_name('li')
    self.assertIn('180', [tag.text for tag in autocomplete_tags])

    # The user selects the '180' autocomplete selection and hits enter
    for tag in autocomplete_tags:
      if tag.text == '180':
        tag.click()
    searchbox.send_keys(Keys.ENTER)

    # The map changes to show only the locations for the movie "180"
    # TODO(eso) figure out how to test for this
    # Testing for the map pins feels like we'd be testing a library
    # Maybe test that the javascript objects are created? If so, we'd
    # have to do that in the JS tests
