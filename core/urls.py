from django.urls import path, include
from snippets import views
from userapp import views

urlpatterns = [
    path('', include('snippets.urls')),
    path('', include('userapp.urls')),
]