from django.core.management.base import BaseCommand
from locations.models import Location

import json
import requests

from sf_movies.settings import SFGOV_API_KEY, SFGOV_API_ENDPOINT


class Command(BaseCommand):
  """Populates the Location database using an Ajax query to SFGOV Films data API. Then make calls to Google's Geocoding API to try to get latitude/longitude coordinates for each entry.
  """

  # args = '<foo bar ...>'
  help = 'Query the SF GOV SODA API to populate the Location database'

  def _query_api(self):
    # The API key is not necessary for querying, see API documentation at
    #  http://dev.socrata.com/docs/app-tokens.html
    params = {}
    headers = {'X-APP-TOKEN': SFGOV_API_KEY}
    resp = requests.get(
      SFGOV_API_ENDPOINT,
      params=params,
      headers=headers
    )

    locations = resp.json()
    for location in locations:
      try:
        new_location = Location.objects.create(**location)
        new_location.save()
      except Exception as err:
        print("Error occured: %s with location %s" % (err, location))

  def handle(self, *args, **options):
    self._query_api()
