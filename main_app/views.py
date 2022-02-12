from django.shortcuts import render
from django.http import HttpResponse


def index(request):
  return HttpResponse('''Hello World, welcome the foodscraper app. Your one stop shop to find all local stores for all your local recipe needs. For the community, by the community and with the community!!''')
# Create your views here.
