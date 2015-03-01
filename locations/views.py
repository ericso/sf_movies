from django.shortcuts import render
from django.http import JsonResponse

import json
import requests


API_ENDPOINT = 'https://data.sfgov.org/resource/yitu-d5am.json'
API_KEY = 'iXBPg47nIqMKX8hBFqot8fTtH'

def locations(request):
  """Returns JSON response containing full query to SF Film API
  """

  search_text = request.GET.get('search_text', None)

  # Make a request to the SF Films API
  params = {}
  if search_text is not None:
    params['title'] = search_text

  headers = {'X-APP-TOKEN': API_KEY}
  resp = requests.get(
    API_ENDPOINT,
    params=params,
    headers=headers
  )

  films = resp.json()

  return_data = {'locations': films}

  return JsonResponse(films, safe=False)
