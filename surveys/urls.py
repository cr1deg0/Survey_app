""" URL configuration for surveys main app """

from django.urls import path
from surveys.views import Home, SurveyEdit, SurveyListView, SurveyCreateView, SurveyDetail

urlpatterns = [
    path('my_surveys/new/', SurveyCreateView.as_view(), name='survey_add'),
    path('my_surveys/<slug:slug>/edit/',
         SurveyEdit.as_view(), name='survey_edit'),
    path('my_surveys/<slug:slug>/', SurveyDetail.as_view(), name='survey_detail'),
    path('my_surveys/', SurveyListView.as_view(), name='survey_list'),
    path('', Home.as_view(), name='home'),
]
