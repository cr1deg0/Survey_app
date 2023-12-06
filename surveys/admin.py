from django.contrib import admin
from guardian.admin import GuardedModelAdmin
from .models import Survey, Question, Option

# Register your models here.


class OptionInLine(admin.TabularInline):
    """ Display Options in tabular mode"""
    model = Option
    extra = 0


class QuestionInLine(admin.StackedInline):
    model = Question
    extra = 0


@admin.register(Survey)
class SurveyAdmin(GuardedModelAdmin):
    """ Display survey title and creation date in admin surveys summary. Display Survey and Questions 
    and together """
    prepopulated_fields = {'slug': ('title',), }
    inlines = [QuestionInLine]
    list_display = ['title', 'created']


@admin.register(Question)
class QuestionAdmin(GuardedModelAdmin):
    """ Display Question and Options together """
    inlines = [OptionInLine]
