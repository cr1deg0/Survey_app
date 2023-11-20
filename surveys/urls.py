""" URL configuration for surveys main app """

from django.urls import path
from surveys.views import Home, SurveyListView

urlpatterns = [
  path('', Home.as_view(), name='home'),
  path('my_surveys/', SurveyListView.as_view(), name='my_surveys'),
]