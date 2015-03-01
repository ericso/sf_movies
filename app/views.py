from django.shortcuts import render
from django.http import HttpResponse


def home(request):
  """Renders the home view of the app
  """
  return render(request, 'home.html', {})
