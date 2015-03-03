from django.core.management.base import BaseCommand
from locations.models import Location

from time import sleep
import json
import requests

from sf_movies.settings import SFGOV_API_KEY, SFGOV_API_ENDPOINT
from sf_movies.settings import GOOGLE_API_KEY, GOOGLE_GEOCODING_ENDNPOINT


class Command(BaseCommand):
  """Populates the Location database using an Ajax query to SFGOV Films data API. Then make calls to Google's Geocoding API to try to get latitude/longitude coordinates for each entry.
  """

  # args = '<foo bar ...>'
  help = 'Query the SF GOV SODA API to populate the Location database'

  def _populate_db(self):
    locations = self._query_sfgov_api()

    for location in locations:
      # Some results from SF GOV API may not contain the location key
      if 'locations' in location:
        coordinates = self._query_google_geocoder(location['locations'])
      else:
        coordinates = False
      # Google Geocode API limits requests to 5 per second, set high
      #  to be safe
      sleep(0.5)
      print(coordinates)

      if coordinates:
        location['latitude'] = coordinates['lat']
        location['longitude'] = coordinates['lng']
      try:
        new_location = Location.objects.create(**location)
        new_location.save()
      except Exception as err:
        # print("Error occured: %s with location %s" % (err, location))
        pass


  def _query_sfgov_api(self):
    """Makes a query to SODA API at SF GOV for film data.

    The API key is not necessary for querying, see API documentation at
    http://dev.socrata.com/docs/app-tokens.html
    """
    params = {}
    headers = {'X-APP-TOKEN': SFGOV_API_KEY}
    resp = requests.get(
      SFGOV_API_ENDPOINT,
      params=params,
      headers=headers
    )
    return resp.json()


  def _query_google_geocoder(self, query_text):
    """Makes a query to the Google Geocoding API to get latitude and longitude data.

    API documentation at
    https://developers.google.com/maps/documentation/geocoding/
    """
    params = {
      'key': GOOGLE_API_KEY,
      'address': query_text,
    }
    resp = requests.get(
      GOOGLE_GEOCODING_ENDNPOINT,
      params=params
    )

    json_resp = resp.json()
    if json_resp['status'] == "OK":
      print(json_resp)
      return json_resp['results'][0]['geometry']['location']
    else:
      print(json_resp['status'])
      print(json_resp)
      return False


  def handle(self, *args, **options):
    self._populate_db()
