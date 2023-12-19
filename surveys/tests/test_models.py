from datetime import datetime
from django.test import TestCase, Client
from django.contrib.auth.models import User
from ..models import Survey, Question, Option
from django.urls import reverse

class SurveyModelTest(TestCase):
  def setUp(self):
    self.user = User.objects.create(
      username='test_user', 
      email='test@email.com',
      password='test_psswd')

    self.survey = Survey.objects.create(
      title = 'test survey',
      author = self.user
    )

  def test_survey_object(self):
    self.assertEqual(self.survey.title, 'test survey')
    self.assertEqual(self.survey.author.username, 'test_user')
    self.assertEqual(self.survey.slug, 'test-survey')
    self.assertIsInstance(self.survey.created, datetime)
    self.assertEqual(self.survey.status, 'DRAFT')
    self.assertEqual(self.survey.submissions, 0)
  
  def test_get_absolute_url(self):
    self.assertEqual(self.survey.get_absolute_url(), '/my_surveys/test-survey/edit/')

  def test_user_general_permissions(self):

    self.assertTrue(self.user.has_perm('surveys.add_survey'))
    self.assertTrue(self.user.has_perm('surveys.change_survey'))
    self.assertTrue(self.user.has_perm('surveys.delete_survey'))
    self.assertTrue(self.user.has_perm('surveys.view_survey'))
  
  def test_user_permissions_to_own_surveys(self):

    self.assertTrue(self.user.has_perm('surveys.view_own_survey', self.survey))
    self.assertTrue(self.user.has_perm('surveys.edit_own_survey', self.survey))
    self.assertTrue(self.user.has_perm('surveys.delete_own_survey', self.survey))
  
  def test_user_no_permissions_to_not_own_survey(self):
    user2 = User.objects.create(
      username='user2', 
      email='user2@email.com',
      password='user2_psswd')
    survey2 = Survey.objects.create(
      title = 'test2 survey',
      author = user2
    )

    self.assertFalse(self.user.has_perm('surveys.view_own_survey', survey2))
    self.assertFalse(self.user.has_perm('surveys.edit_own_survey', survey2))
    self.assertFalse(self.user.has_perm('surveys.delete_own_survey', survey2))


class QuestionModelTest(TestCase):
  def setUp(self):
    self.user = User.objects.create(username='test_user', password='test_psswd')
    self.survey = Survey.objects.create(title = 'test survey', author = self.user)
    self.question = Question.objects.create(survey=self.survey, question='test question')

  def test_question_object(self):
    self.assertEqual(self.question.survey.title, 'test survey')
    self.assertEqual(self.question.question, 'test question')

  def test_get_absolute_url(self):
    self.assertEqual(self.question.get_absolute_url(), '/my_surveys/test-survey/edit/')
  
  def test_user_permissions_to_own_questions(self):

    self.assertTrue(self.user.has_perm('surveys.view_own_question', self.question))
    self.assertTrue(self.user.has_perm('surveys.edit_own_question', self.question))
    self.assertTrue(self.user.has_perm('surveys.delete_own_question', self.question))
  
  def test_user_no_permissions_to_not_own_questions(self):

    user2 = User.objects.create(
      username='user2', 
      email='user2@email.com',
      password='user2_psswd')
    survey2 = Survey.objects.create(
      title = 'test2 survey',
      author = user2
    )
    question2 = Question.objects.create(survey=survey2, question='test question 2')
    self.assertFalse(self.user.has_perm('surveys.view_own_question', question2))
    self.assertFalse(self.user.has_perm('surveys.edit_own_question', question2))
    self.assertFalse(self.user.has_perm('surveys.delete_own_question', question2))

class OptionModelTest(TestCase):
  def setUp(self):
    self.user = User.objects.create(username='test_user', password='test_psswd')
    self.survey = Survey.objects.create(title = 'test survey', author = self.user)
    self.question = Question.objects.create(survey=self.survey, question='test question')
    self.option = Option.objects.create(question=self.question, option='test option')

  def test_option_object(self):
    self.assertEqual(self.option.question.question, 'test question')
    self.assertEqual(self.option.option, 'test option')
    self.assertEqual(self.option.question.survey.title, 'test survey')

  def test_get_absolute_url(self):
    self.assertEqual(self.option.get_absolute_url(), '/my_surveys/test-survey/edit/')