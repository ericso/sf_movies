from django.shortcuts import render
from django.http import JsonResponse

import json


def locations(request):

  if request.is_ajax():
    print("request is ajax")
  else:
    print("request is NOT ajax")

  data = {'key': 'value'}
  return JsonResponse(data)
