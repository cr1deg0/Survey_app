from django.views.generic import (ListView, DetailView, UpdateView,
CreateView, TemplateView, FormView, DeleteView)
from django.views.generic.detail import SingleObjectMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from surveys.forms import EditSurveyForm
from surveys.models import Question, Survey
from guardian.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy, reverse
from django.shortcuts import HttpResponseRedirect
from .forms import SurveyQuestionsFormset, QuestionOptionsFormset


class Home(TemplateView):
  """ Home page view """
  template_name = 'home.html'

class SurveyListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
  """ View of the user's surveys """
  model = Survey
  context_object_name = 'surveys'
  template_name = 'surveys/dashboard.html'
  permission_required='surveys.view_survey'

  def get_queryset(self):
    return Survey.objects.filter(author=self.request.user)

class SurveyCreateView(LoginRequiredMixin, CreateView):
  """ 
  Create a new survey view. Bind the survey to the user and asign relevant permissions. 
  """
  model = Survey
  fields = ['title']
  template_name = 'surveys/new.html'

  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)

#  TO DO 
class SurveyDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
  """ View the details of the survey responses """
  model = Survey
  template_name = 'surveys/detail.html'
  context_object_name = 'survey'
  permission_required='surveys.view_own_survey'

class SurveyDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
  """ Deletes a Survey instance """
  model=Survey
  template_name='surveys/delete.html'
  content_object_name = 'survey'
  success_url = reverse_lazy('survey_list')
  permission_required='surveys.delete_own_survey'

class SurveyEdit(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
  """ View to change survey title and status. Lists the questions already in the survey. Links to a new view to add or modify questions. Links to a view to add or modify question answer options."""
  model = Survey
  form_class = EditSurveyForm
  template_name= 'surveys/edit.html'
  permission_required='surveys.edit_own_survey'


  def get_success_url(self):
    return reverse_lazy('survey_edit', args=[self.kwargs['slug']])


class SurveyQuestionsEditView(LoginRequiredMixin, PermissionRequiredMixin, SingleObjectMixin, FormView):
  model = Survey
  template_name = 'surveys/edit_questions.html'
  permission_required=('surveys.edit_own_survey', 'surveys.view_own_survey', 'surveys.delete_own_survey')

  def get(self, request, *args, **kwargs):
    """ Get the survey object associated with 'slug' argument in the 
    http request GET URLConf. Assign the object to the new instance attribue self.object """
    self.object = self.get_object(queryset=Survey.objects.all())
    return super().get(request, *args, **kwargs)

  def post(self, request, *args, **kwargs ):
    self.object = self.get_object(queryset=Survey.objects.all())
    return super().post(request, *args, **kwargs)

  def get_form(self, form_class=None):
    return SurveyQuestionsFormset(**self.get_form_kwargs(), instance=self.object)
  
  def form_valid(self, form):
    form.save()
    return HttpResponseRedirect(self.get_success_url())
  
  def get_success_url(self):
    return reverse('survey_edit', kwargs = {'slug': self.object.slug })


class QuestionOptionsEditView(LoginRequiredMixin, PermissionRequiredMixin, SingleObjectMixin, FormView):
  model = Question
  template_name = 'surveys/edit_question_options.html'
  permission_required= ('surveys.edit_own_question', 'surveys.view_own_question', 'surveys.delete_own_question')

  def get(self, request, *args, **kwargs):
    self.object = self.get_object(queryset=Question.objects.all())
    return super().get(request, *args, **kwargs)

  def post(self, request, *args, **kwargs ):
    self.object = self.get_object(queryset=Question.objects.all())
    return super().post(request, *args, **kwargs)

  def get_form(self, form_class=None):
    return QuestionOptionsFormset(**self.get_form_kwargs(), instance=self.object)

  def form_valid(self, form):
    form.save()
    return HttpResponseRedirect(self.get_success_url())
  
  def get_success_url(self):
    return reverse('survey_edit', kwargs = {'slug': self.object.survey.slug })