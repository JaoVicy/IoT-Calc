from django.shortcuts import render
from django.http import HttpResponse

# for def distance_calculator:
from django.shortcuts import render
from .form import DistanceForm
from geopy.distance import geodesic


def index(request):

    try:
        result = None
        if request.method == "POST":
            form = DistanceForm(request.POST)
            if form.is_valid():
                lat1 = form.cleaned_data["lat1"]
                lon1 = form.cleaned_data["lon1"]
                lat2 = form.cleaned_data["lat2"]
                lon2 = form.cleaned_data["lon2"]
                point1 = (lat1, lon1)
                point2 = (lat2, lon2)
                distance = geodesic(point1, point2).kilometers
                result = f"{distance:.2f} km"
        else:
            form = DistanceForm()

    except ValueError:
        return HttpResponse("Invalid input. Please enter valid coordinates.")   
    except Exception as e:
        return HttpResponse(f"An error occurred: {e}")
    
        return render(request, "app/index.html", {"form": form, "result": result})


""""
# Function to handle distance calculation (future use)
def distance_calculator(request):
    result = None
    if request.method == "POST":
        form = DistanceForm(request.POST)
        if form.is_valid():
            lat1 = form.cleaned_data["lat1"]
            lon1 = form.cleaned_data["lon1"]
            lat2 = form.cleaned_data["lat2"]
            lon2 = form.cleaned_data["lon2"]
            point1 = (lat1, lon1)
            point2 = (lat2, lon2)
            distance = geodesic(point1, point2).kilometers
            result = f"{distance:.2f} km"
    else:
        form = DistanceForm()
    return render(request, "distance_form.html", {"form": form, "result": result})
"""
