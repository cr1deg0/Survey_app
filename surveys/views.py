from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from surveys.models import Survey


# Create your views here.

class Home(TemplateView):
  """ Home page view """
  template_name = 'home.html'

class SurveyListView(ListView):
  model = Survey
  context_object_name = 'surveys'

class SurveyEdit(DetailView):
  model = Survey
  template_name= 'surveys/edit.html'