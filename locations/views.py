import json
import requests

from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from django.db.models import Q

from locations.models import Location


def locations(request):
  """Returns JSON response containing full query to SF Film API
  """

  search = request.GET.get('search', None)
  if search is not None:
    print("Search text is %s" % (search,))

    qs = Location.objects.filter(
      Q(title__contains=search) |
      Q(locations__contains=search) |
      Q(fun_facts__contains=search) |
      Q(production_company__contains=search) |
      Q(distributor__contains=search) |
      Q(director__contains=search) |
      Q(writer__contains=search) |
      Q(actor_1__contains=search) |
      Q(actor_2__contains=search) |
      Q(actor_3__contains=search)
    )
  else:
    qs = Location.objects.all()

  json_data = serializers.serialize('json', qs)

  # The front-end is using Backbonejs and currently expects the response to
  #  be a list of dictionaries. Django's JsonResponse's safe parameter
  #  needs to be explicitly set to false to allow non-dictionary return
  #  values.
  return JsonResponse(json.loads(json_data), safe=False)
