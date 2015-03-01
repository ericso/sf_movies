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

    data = json.loads(response.content.decode())

    single_film = {
      "actor_1": "Siddarth",
      "actor_2": "Nithya Menon",
      "actor_3": "Priya Anand",
      "director": "Jayendra",
      "locations": "Epic Roasthouse (399 Embarcadero)",
      "production_company": "SPI Cinemas",
      "release_year": "2011",
      "title": "180",
      "writer": "Umarji Anuradha, Jayendra, Aarthi Sriram, & Suba "
    }

    self.assertIn(single_film, data['films'])

  def test_location_route_takes_search_parameter(self):
    response = self.client.get(
      '/locations/',
      {'search_text': '180'},
      HTTP_X_REQUESTED_WITH='XMLHttpRequest'
    )

    data = json.loads(response.content.decode())

    single_film = {
      "actor_1": "Sarah Jones",
      "actor_2": "Elizabeth Sarnoff",
      "actor_3": "Bryan Wynbrandt",
      "director": "J.J. Abrams",
      "distributor": "Warner Bros. Television",
      "locations": "Taylor St. from Broadway to Filbert",
      "production_company": "Bonanza Productions Inc.",
      "release_year": "2012",
      "title": "Alcatraz",
      "writer": "Steven Lilien"
    }

    self.assertNotIn(single_film, data['films'])
