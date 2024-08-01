from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from userapp import views

urlpatterns = [
    path('users/', views.user_list),
    path('users/<int:pk>/', views.user_details),
]

urlpatterns = format_suffix_patterns(urlpatterns)