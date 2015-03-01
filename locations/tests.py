from django.test import TestCase

import json


class ApiTest(TestCase):
  """Test class for locations Api

  Routes:
  GET /locations - Returns JSON containing all locations
  GET /locations/:search_text - Returns JSON containing locations filtered by the search_text
  """

  def test_location_route_returns_200(self):
    response = self.client.get(
      '/locations/',
      HTTP_X_REQUESTED_WITH='XMLHttpRequest'
    )
    self.assertEqual(response.status_code, 200)


  def test_location_route_returns_list(self):

    response = self.client.get(
      '/locations/',
      HTTP_X_REQUESTED_WITH='XMLHttpRequest'
    )

    data = json.loads(response.content.decode())

    self.assertIsInstance(data, type([]), "Response is not a list")


  def test_location_route_takes_search_parameter(self):

    # Gibberish search text should cause request to return an empty list
    response = self.client.get(
      '/locations/',
      {'search_text': 'asdfasdfasdfasdfasdf0owkd'},
      HTTP_X_REQUESTED_WITH='XMLHttpRequest'
    )

    data = json.loads(response.content.decode())

    self.assertFalse(data)
