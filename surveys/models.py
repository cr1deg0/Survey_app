from django.db import models

# Create your models here.

class Survey(models.Model):
  """ Model of a Survey """
  STATUS = [
    ("DRAFT", "Draft"),
    ("ACTIVE", "Active"),
  ]
  title = models.CharField(max_length=250, unique=True)
  creation_date = models.DateTimeField(auto_now_add=True)
  status = models.CharField(max_length=6, choices=STATUS, default=STATUS[0][0])
  submissions = models.IntegerField(default=0)

class Question(models.Model):
  survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
  question = models.CharField(max_length=250)

class Option(models.Model):
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  option = models.CharField(max_length=250)
  selected = models.IntegerField(default=0)
