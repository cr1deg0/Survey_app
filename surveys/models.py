from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Survey(models.Model):
  """ Model of a Survey """
  STATUS = [
    ("DRAFT", "Draft"),
    ("ACTIVE", "Active"),
  ]
  title = models.CharField(max_length=250, unique=True)
  creator = models.ForeignKey(User, on_delete=models.CASCADE)
  creation_date = models.DateTimeField(auto_now_add=True)
  status = models.CharField(max_length=6, choices=STATUS, default=STATUS[0][0])
  submissions = models.IntegerField(default=0)

  def __str__(self):
    return self.title

  def absolute_url(self):
    return reverse('survey_list')

class Question(models.Model):
  survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
  question = models.CharField(max_length=250)

  def __str__(self):
      return self.question

class Option(models.Model):
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  option = models.CharField(max_length=250)
  selected = models.IntegerField(default=0)

  def __str__(self):
    return self.option