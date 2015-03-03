import json

from django.test import TestCase

from locations.models import Location


class ApiTest(TestCase):
  """Test class for locations Api

  Routes:
  GET /locations/ - Returns JSON containing all locations
  GET /locations/:search_text - Returns JSON containing locations filtered by the search_text
  """

  def setUp(self):
    """Create a test location in the database
    """
    self.location_params = {
      'title': "A Fridge Too Far",
      'locations': "My House",
    }
    new_location = Location.objects.create(**self.location_params)
    new_location.save()

  def tearDown(self):
    """Clear test database
    """
    Location.objects.all().delete()

  def _query_api(self, **kwargs):
    response = self.client.get(
      '/locations/',
      HTTP_X_REQUESTED_WITH='XMLHttpRequest',
      data=kwargs
    )
    return json.loads(response.content.decode())

  ### Test Methods ###
  def test_location_route_returns_200(self):
    response = self.client.get(
      '/locations/',
      HTTP_X_REQUESTED_WITH='XMLHttpRequest'
    )
    self.assertEqual(response.status_code, 200)

  def test_location_route_returns_list(self):
    data = self._query_api()
    self.assertIsInstance(data, type([]), "Response is not a list")

  def test_location_route_returns_expected_result(self):
    data = self._query_api()
    self.assertIn(self.location_params['title'], data[0]['fields']['title'])
    self.assertIn(self.location_params['locations'], data[0]['fields']['locations'])

  def test_location_route_takes_search_parameter(self):
    """Send query with search string. This should not return our expected result.
    """
    data = self._query_api(search='some search text')
    self.assertFalse(data)
