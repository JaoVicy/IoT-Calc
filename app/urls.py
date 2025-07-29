from django.urls import include, path
from app.views import index

urlpatterns = [
    path('', index) # This will route the root URL to the index view
]