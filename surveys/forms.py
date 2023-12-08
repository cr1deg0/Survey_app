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
     Survey, Question, fields=('question',), extra=1)

QuestionOptionsFormset = inlineformset_factory(
    Question, Option, fields=('option',), extra=2
)