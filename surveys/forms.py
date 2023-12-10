from django import forms
from .models import Survey, Question, Option
from django.forms.models import inlineformset_factory, BaseInlineFormSet


class EditSurveyForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = ('title', 'status')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.RadioSelect()
        }


# Define the models the inline form is working with
SurveyQuestionsFormset = inlineformset_factory(
     Survey, 
     Question, 
     fields=('question',), 
     extra=3,
     widgets={'question': forms.TextInput(attrs={'class': 'form-control'})},
)

QuestionOptionsFormset = inlineformset_factory(
    Question, 
    Option, 
    fields=('option',), 
    extra=3,
    widgets={'option': forms.TextInput(attrs={'class': 'form-control'})},
)