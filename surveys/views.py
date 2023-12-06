from django.views.generic import ListView, DetailView, UpdateView, CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from surveys.forms import EditSurveyForm
from surveys.models import Survey
from guardian.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy


class Home(TemplateView):
  """ Home page view """
  template_name = 'home.html'

class SurveyListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
  model = Survey
  context_object_name = 'surveys'
  template_name = 'surveys/dashboard.html'
  permission_required='surveys.view_survey'

  def get_queryset(self):
    # return super().get_queryset().filter(author=self.request.user)
    return Survey.objects.filter(author=self.request.user)

class SurveyDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
  """ View the details of the survey responses """
  model = Survey
  template_name = 'surveys/detail.html'
  context_object_name = 'survey'
  permission_required='surveys.view_own_survey'


class SurveyEdit(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
  """ Edit survey """
  model = Survey
  form_class = EditSurveyForm
  template_name= 'surveys/edit.html'
  permission_required='surveys.view_own_survey'
  # success_url = reverse_lazy('survey_edit', args=[])

  def get_success_url(self):
    print(self.kwargs)
    return reverse_lazy('survey_edit', args=[self.kwargs['slug']])

class SurveyNew(LoginRequiredMixin, CreateView):
  model = Survey
  fields = ['title']
  template_name = 'surveys/new.html'

  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)

