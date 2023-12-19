""" URL configuration for surveys main app """

from django.urls import path
from surveys.views import (Home, SurveyEdit, SurveyListView,
SurveyCreateView, SurveyDetail, SurveyQuestionsEditView, 
QuestionOptionsEditView, SurveyDeleteView)

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('my_surveys/', SurveyListView.as_view(), name='survey_list'),
    path('my_surveys/new/', SurveyCreateView.as_view(), name='survey_add'),
    path('my_surveys/<slug:slug>/results', SurveyDetail.as_view(), name='survey_detail'),
    path('my_surveys/<slug:slug>/delete', SurveyDeleteView.as_view(), name='survey_delete'),
    path('my_surveys/<slug:slug>/edit/',
         SurveyEdit.as_view(), name='survey_edit'),
    path('my_surveys/<slug:slug>/edit/add_question',
         SurveyQuestionsEditView.as_view(), name='questions_edit'),
     path('my_surveys/<slug:slug>/edit/<int:pk>/add_options',
         QuestionOptionsEditView.as_view(), name='options_edit'),
]
