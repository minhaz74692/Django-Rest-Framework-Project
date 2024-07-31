from django.urls import path, include
from snippets import views

urlpatterns = [
    path('', include('snippets.urls')),
]