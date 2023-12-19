from django.test import TestCase
from django.contrib.auth.models import User
from ..models import Survey, Question, Option
from django.urls import reverse

class HomePageViewTest(TestCase):

  def test_home_page_status_code(self):
    response = self.client.get('/')
    self.assertEqual(response.status_code, 200)

  def test_view_uses_correct_template(self):
    response = self.client.get(reverse('home'))
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'home.html')

class LoginView(TestCase):
  
  def test_login_url_exists(self):
    response = self.client.get('/accounts/login/')
    self.assertEqual(response.status_code, 200)
  
  def test_login_url_by_name(self):
    response = self.client.get(reverse('login'))
    self.assertEqual(response.status_code, 200)

  def test_login_template(self):
    response = self.client.get(reverse('login'))
    self.assertTemplateUsed(response, 'registration/login.html')


class SignUpView(TestCase):
  
  def test_signup_url_exists(self):
    response = self.client.get('/accounts/signup/')
    self.assertEqual(response.status_code, 200)
  
  def test_login_url_by_name(self):
    response = self.client.get(reverse('signup'))
    self.assertEqual(response.status_code, 200)

  def test_login_template(self):
    response = self.client.get(reverse('signup'))
    self.assertTemplateUsed(response, 'registration/signup.html')


