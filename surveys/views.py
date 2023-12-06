from django.views.generic import ListView, DetailView, UpdateView, CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from surveys.models import Survey
from guardian.mixins import PermissionRequiredMixin

# Create your views here.

# class UserAccessMixin(LoginRequiredMixin, UserPassesTestMixin):
#   def get_test_func(self):
#     if not self.request.user == Survey.
#     return super().get_test_func()

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
  model = Survey
  template_name = 'surveys/detail.html'
  context_object_name = 'survey'
  permission_required='surveys.view_own_survey'

  def get_context_data(self, **kwargs):
    print(self.kwargs)
    return super().get_context_data(**kwargs)

class SurveyEdit(LoginRequiredMixin, UpdateView):
  model = Survey
  template_name= 'surveys/edit.html'

class SurveyNew(LoginRequiredMixin, CreateView):
  model = Survey
  fields = ['title']
  template_name = 'surveys/new.html'

  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)

