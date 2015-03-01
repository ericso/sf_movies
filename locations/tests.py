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

  def test_location_route_returns_json(self):

    response = self.client.get(
      '/locations/',
      HTTP_X_REQUESTED_WITH='XMLHttpRequest'
    )
    data = response.content.decode()

    self.assertEqual(json.loads(data), {'key': 'value'})

