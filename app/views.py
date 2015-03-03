from django.shortcuts import render
from django.http import HttpResponse

from sf_movies.settings import GOOGLE_API_KEY


def home(request):
  """Renders the home view of the app
  """
  return render(request, 'home.html', {'GOOGLE_API_KEY': GOOGLE_API_KEY})
