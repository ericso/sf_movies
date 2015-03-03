from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class NewVisitorTest(unittest.TestCase):

  def setUp(self):
    self.browser = webdriver.Chrome()
    self.browser.implicitly_wait(3)

  def tearDown(self):
    self.browser.quit()


  ### Helper Methods ###


  ### Test Methods ###
  def test_can_see_map_a_filter_by_search_text(self):
    # The user goes to the web site
    self.browser.get('http://localhost:8000')

    # The user sees a search box at the top of the page
    searchbox = self.browser.find_element_by_id('id_search')

    # The user then also sees a map below the search box
    map_area = self.browser.find_element_by_id('id_map')

    # The user decides to filter for the movie "180"
    searchbox.send_keys('180')
    searchbox.send_keys(Keys.ENTER)

    # The map changes to show only the locations for the movie "180"


    self.fail('Finish the test!')


if __name__ == '__main__':
  unittest.main(warnings='ignore')
