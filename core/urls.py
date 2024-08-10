from django.urls import path, include
from snippets import views
from userapp import views
from django.contrib import admin
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('', include('snippets.urls')),
    path('', include('userapp.urls')),
    path('admin/', admin.site.urls),
]