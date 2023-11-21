""" URL configuration for surveys main app """

from django.urls import path
from surveys.views import Home, SurveyEdit, SurveyListView

urlpatterns = [
  path('my_surveys/<int:pk>/edit/', SurveyEdit.as_view(), name='survey_edit'),
  path('my_surveys/', SurveyListView.as_view(), name='survey_list'),
  path('', Home.as_view(), name='home'),
]