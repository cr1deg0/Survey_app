import pytest
from surveys.forms import (
    AnswerForm,
    EditSurveyForm,
    QuestionOptionsFormset,
    SurveyQuestionsFormset,
)

pytestmark = pytest.mark.django_db


class TestEditSurveyForm:
    form = EditSurveyForm()

    def test_title_field_label(self):
        assert self.form.fields["title"].label == "Title"

    def test_status_field_label(self):
        assert self.form.fields["status"].label == "Status"


class TestSurveyQuestionsFormset:
    form = SurveyQuestionsFormset()

    def test_question_field_label(self):
        assert self.form[0].fields["question"].label == "Question"
        assert self.form[1].fields["question"].label == "Question"
        assert self.form[2].fields["question"].label == "Question"


class TestQuestionOptionsFormset:
    form = QuestionOptionsFormset()

    def test_option_field_label(self):
        assert self.form[0].fields["option"].label == "Option"
        assert self.form[1].fields["option"].label == "Option"
        assert self.form[2].fields["option"].label == "Option"


class TestAnswerForm:
    def test_options_field_label(self, option_factory, question_factory):
        question = question_factory()
        option1 = option_factory(option="option1", question=question)
        option2 = option_factory(option="option2", question=question)
        form = AnswerForm(options=[option1, option2])

        assert "option1" in form.fields["options"].choices[0]
        assert "option2" in form.fields["options"].choices[1]
