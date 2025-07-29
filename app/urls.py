from django.urls import include, path
from app.views import index

urlpatterns = [
    path('', index) 
]