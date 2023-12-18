from django import forms
from .models import Survey, Question, Option
from django.forms.models import inlineformset_factory


class EditSurveyForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = ('title', 'status')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.RadioSelect()
        }


# Inline form to allow displaying more than one question associatd with a specific survey in the same form
SurveyQuestionsFormset = inlineformset_factory(
     Survey, 
     Question, 
     fields=('question',), 
     extra=3,
     widgets={'question': forms.TextInput(attrs={'class': 'form-control'})},
)
# Inline form to allow displaying more than one option associated with a specific question in the same form
QuestionOptionsFormset = inlineformset_factory(
    Question, 
    Option, 
    fields=('option',), 
    extra=3,
    widgets={'option': forms.TextInput(attrs={'class': 'form-control'})},
)