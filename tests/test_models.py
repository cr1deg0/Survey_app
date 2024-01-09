from datetime import datetime

import pytest

pytestmark = pytest.mark.django_db


class TestSurveyModel:
    def test_survey_object(self, survey):
        assert survey.title == "survey1"
        assert survey.author.username == "user1"
        assert survey.slug == "survey1"
        assert isinstance(survey.created, datetime)
        assert survey.status == "DRAFT"
        assert survey.submissions == 0

    def test_slugify_on_save(self, survey_factory):
        survey = survey_factory(title="test survey")
        assert survey.slug == "test-survey"

    def test_get_absolute_url_method(self, survey):
        assert survey.get_absolute_url() == "/my_surveys/survey1/edit/"

    def test_str_method(self, survey):
        assert survey.__str__() == "survey1"

    def test_user_general_permissions(self, user):
        assert user.has_perm("surveys.add_survey")
        assert user.has_perm("surveys.change_survey")
        assert user.has_perm("surveys.delete_survey")
        assert user.has_perm("surveys.view_survey")

    def test_user_has_permissions_to_own_surveys(self, user, survey):
        assert user.has_perm("surveys.view_own_survey", survey)
        assert user.has_perm("surveys.edit_own_survey", survey)
        assert user.has_perm("surveys.delete_own_survey", survey)

    def test_user_has_no_permissions_to_not_own_survey(self, survey, user_factory):
        user2 = user_factory(username="user2")

        assert not user2.has_perm("surveys.view_own_survey", survey)
        assert not user2.has_perm("surveys.edit_own_survey", survey)
        assert not user2.has_perm("surveys.delete_own_survey", survey)


class TestQuestionModel:
    def test_question_object(self, question):
        assert question.survey.title == "survey1"
        assert question.question == "question1"

    def test_get_absolute_url_method(self, question):
        assert question.get_absolute_url() == "/my_surveys/survey1/edit/"

    def test_str_method(self, question):
        assert question.__str__() == "question1"

    def test_user_has_permissions_to_own_questions(self, user, question):
        assert user.has_perm("surveys.view_own_question", question)
        assert user.has_perm("surveys.edit_own_question", question)
        assert user.has_perm("surveys.delete_own_question", question)

    def test_user_has_no_permissions_to_not_own_questions(self, question, user_factory):
        user2 = user_factory(username="user 2")
        assert not user2.has_perm("surveys.view_own_question", question)
        assert not user2.has_perm("surveys.edit_own_question", question)
        assert not user2.has_perm("surveys.delete_own_question", question)


class TestOptionModel:
    def test_option_object(self, option):
        assert option.question.question == "question1"
        assert option.option == "option1"
        assert option.question.survey.title == "survey1"

    def test_get_absolute_url_method(self, option):
        assert option.get_absolute_url() == "/my_surveys/survey1/edit/"

    def test_str_method(self, option):
        assert option.__str__() == "option1"
