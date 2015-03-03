from django.shortcuts import render
from django.http import HttpResponse


def home(request):
  """Renders the home view of the app
  """
  return render(request, 'home.html', {'GOOGLE_API_KEY': 'AIzaSyCq2vRo28y8UnbW2kwxn2oihcXBc0eH1iE'})
