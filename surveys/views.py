from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
# from django.views import Views

# Create your views here.

class Home(TemplateView):
  """ Home page view """
  template_name = 'home.html'


class My_Surveys(TemplateView):
  template_name = 'my_surveys.html'