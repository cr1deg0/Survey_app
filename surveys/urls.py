""" URL configuration for surveys main app """

from django.urls import path
from surveys.views import Home, My_Surveys

urlpatterns = [
  path('', Home.as_view(), name='home'),
  path('my_surveys/', My_Surveys.as_view(), name='my_surveys'),
]