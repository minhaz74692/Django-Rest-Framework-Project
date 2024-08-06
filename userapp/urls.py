from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from userapp import views

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('sign-up/', views.UserRegistration.as_view()),
    path('users/<int:pk>/', views.UserDetails.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)