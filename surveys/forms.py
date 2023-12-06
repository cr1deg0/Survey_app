from django import forms
from .models import Survey


class EditSurveyForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = ('title', 'status')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.RadioSelect()
        }
