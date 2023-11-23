from django.views.generic import ListView, DetailView, UpdateView, CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from surveys.models import Survey

# Create your views here.

class Home(TemplateView):
  """ Home page view """
  template_name = 'home.html'

class SurveyListView(LoginRequiredMixin, ListView):
  model = Survey
  context_object_name = 'surveys'
  template_name = 'surveys/dashboard.html'

  def get_queryset(self):
    return super().get_queryset().filter(creator=self.request.user)

class SurveyEdit(LoginRequiredMixin, UpdateView):
  model = Survey
  template_name= 'surveys/edit.html'

class SurveyNew(LoginRequiredMixin, CreateView):
  model = Survey
  fields = ['title']
  template_name = 'surveys/new.html'

  def form_valid(self, form):
    form.instance.creator = self.request.user
    return super().form_valid(form)

class SurveyDetail(DetailView):
  model = Survey
  template_name = 'surveys/detail.html'
  context_object_name = 'survey'

  def get_context_data(self, **kwargs):
      print(self.kwargs)
      return super().get_context_data(**kwargs)