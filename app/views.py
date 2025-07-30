from django.shortcuts import render
from django.http import HttpResponse

# for def distance_calculator:
from django.shortcuts import render
from .form import DistanceForm
from geopy.distance import geodesic

def index(request):
    return render(request, 'app/index.html')