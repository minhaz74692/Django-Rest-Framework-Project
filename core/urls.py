from django.urls import path, include
from snippets import views
from userapp import views
from django.contrib import admin
from rest_framework.authtoken import views


urlpatterns = [
    path('', include('snippets.urls')),
    path('', include('userapp.urls')),
    path('admin/', admin.site.urls),
    path('api-token-auth/', views.obtain_auth_token),
]