import json
import requests

from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers

from locations.models import Location


def locations(request):
  """Returns JSON response containing full query to SF Film API
  """

  search_text = request.GET.get('search_text', None)

  # Make a request to the SF Films API
  params = {}
  if search_text is not None:
    params['title'] = search_text

  query_data = Location.objects.all()
  json_data = serializers.serialize('json', query_data)

  # The front-end is using Backbonejs and currently expects the response to
  #  be a list of dictionaries. Django's JsonResponse's safe parameter
  #  needs to be explicitly set to false to allow non-dictionary return
  #  values.
  return JsonResponse(json.loads(json_data), safe=False)
