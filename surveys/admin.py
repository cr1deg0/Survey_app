from django.contrib import admin
from .models import Survey, Question, Option

# Register your models here.

class OptionInLine(admin.TabularInline):
  """ Display Options in tabular mode"""
  model = Option
  extra = 0

class QuestionInLine(admin.StackedInline):
  model = Question
  extra = 0

class SurveyAdmin(admin.ModelAdmin):
  """ Display survey title and creation date in admin surveys summary. Display Survey and Questions 
  and together """
  inlines = [QuestionInLine]
  list_display = ['title', 'creation_date']

class QuestionAdmin(admin.ModelAdmin):
  """ Display Question and Options together """
  inlines = [OptionInLine]


admin.site.register(Survey, SurveyAdmin)
admin.site.register(Question, QuestionAdmin)