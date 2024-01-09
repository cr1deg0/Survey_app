import pytest
from django.test import Client
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed
from surveys.models import Survey

pytestmark = pytest.mark.django_db


class TestHomeView:
    client = Client()

    def test_home_view_url_exists(self):
        response = self.client.get("/")
        assert response.status_code == 200

    def test_home_view_url_by_name(self):
        response = self.client.get(reverse("home"))
        assert response.status_code == 200

    def test_home_view_template(self):
        response = self.client.get(reverse("home"))
        assertTemplateUsed(response, "home.html")


class TestLoginView:
    client = Client()

    def test_login_view_url_exists(self):
        response = self.client.get("/accounts/login/")
        assert response.status_code == 200

    def test_login_view_url_by_name(self):
        response = self.client.get(reverse("login"))
        assert response.status_code == 200

    def test_login_view_template(self):
        response = self.client.get(reverse("login"))
        assertTemplateUsed(response, "registration/login.html")


class TestSignUpView:
    client = Client()

    def test_signup_view_url_exists(self):
        response = self.client.get("/accounts/signup/")
        assert response.status_code == 200

    def test_login_view_url_by_name(self):
        response = self.client.get(reverse("signup"))
        assert response.status_code == 200

    def test_login_view_template(self):
        response = self.client.get(reverse("signup"))
        assertTemplateUsed(response, "registration/signup.html")


class TestSurveyListView:
    client = Client()

    def test_survey_list_view_url_exists(self, user_factory):
        user = user_factory()
        self.client.force_login(user=user)

        response = self.client.get("/my_surveys/")
        assert response.status_code == 200

    def test_survey_list_url_by_name(self, user_factory):
        user = user_factory()
        self.client.force_login(user=user)

        response = self.client.get(reverse("survey_list"))
        assert response.status_code == 200

    def test_survey_list_view_template(self, user_factory):
        user = user_factory()
        self.client.force_login(user=user)

        response = self.client.get(reverse("survey_list"))
        assertTemplateUsed(response, "surveys/dashboard.html")

    def test_survey_list_view_has_one_survey(self, survey_factory, user_factory):
        """Test that there is one survey in the rendered list view"""
        user = user_factory()
        survey = survey_factory(author=user)
        self.client.force_login(user=user)

        response = self.client.get(reverse("survey_list"))
        assert len(response.context[-1]["surveys"]) == 1
        assert survey in response.context[-1]["surveys"]

    def test_survey_list_view_has_many_surveys(self, survey_factory, user_factory):
        """Test that there are tow durvyes in the rendered list view"""
        user = user_factory()
        survey = survey_factory(author=user)
        survey2 = survey_factory(title="survey2", author=user)
        self.client.force_login(user=user)

        response = self.client.get(reverse("survey_list"))
        assert len(response.context[-1]["surveys"]) == 2
        assert survey in response.context[-1]["surveys"]
        assert survey2 in response.context[-1]["surveys"]


class TestSurveyCreateView:
    client = Client()

    def test_survey_create_view_url_exists(self, user_factory):
        user = user_factory()
        self.client.force_login(user=user)

        response = self.client.get("/my_surveys/new/")
        assert response.status_code == 200

    def test_survey_create_url_by_name(self, user_factory):
        user = user_factory()
        self.client.force_login(user=user)

        response = self.client.get(reverse("survey_add"))
        assert response.status_code == 200

    def test_survey_create_view_template(self, user_factory):
        user = user_factory()
        self.client.force_login(user=user)

        response = self.client.get(reverse("survey_add"))
        assertTemplateUsed(response, "surveys/new.html")

    def test_survey_create_view_author_added(self, user_factory):
        user = user_factory()
        self.client.force_login(user=user)

        self.client.post("/my_surveys/new/", {"title": "survey1"})
        assert Survey.objects.last().title == "survey1"
        assert Survey.objects.last().author == user


class TestSurveyDetailView:
    client = Client()

    def test_survey_detail_view_url_exists(self, user_factory, survey_factory):
        user = user_factory()
        survey = survey_factory(author=user)
        self.client.force_login(user=user)

        response = self.client.get(f"/my_surveys/{survey.slug}/results/")
        assert response.status_code == 200

    def test_survey_detail_url_by_name(self, user_factory, survey_factory):
        user = user_factory()
        survey = survey_factory(author=user)
        self.client.force_login(user=user)

        response = self.client.get(reverse("survey_detail", args=[survey.slug]))
        assert response.status_code == 200

    def test_survey_detail_view_template(self, user_factory, survey_factory):
        user = user_factory()
        survey = survey_factory(author=user)
        self.client.force_login(user=user)

        response = self.client.get(reverse("survey_detail", args=[survey.slug]))
        assertTemplateUsed(response, "surveys/detail.html")

    def test_survey_detail_view_context(self, option_factory):
        option = option_factory(selected=2)
        survey = option.question.survey
        self.client.force_login(user=survey.author)

        response = self.client.get(reverse("survey_detail", args=[survey.slug]))
        assert response.context[-1]["survey"] == survey
        assert "question1" in response.context[-1]["results"]
        assert "option1" in response.context[-1]["results"]["question1"]
        assert response.context[-1]["results"]["question1"]["option1"] == 2


class TestSurveyDeleteView:
    client = Client()

    def test_survey_delete_view_url_exists(self, user_factory, survey_factory):
        user = user_factory()
        survey = survey_factory(author=user)
        self.client.force_login(user=user)

        response = self.client.get(f"/my_surveys/{survey.slug}/delete/")
        assert response.status_code == 200

    def test_survey_delete_url_by_name(self, user_factory, survey_factory):
        user = user_factory()
        survey = survey_factory(author=user)
        self.client.force_login(user=user)

        response = self.client.get(reverse("survey_delete", args=[survey.slug]))
        assert response.status_code == 200

    def test_survey_delete_view_template(self, user_factory, survey_factory):
        user = user_factory()
        survey = survey_factory(author=user)
        self.client.force_login(user=user)

        response = self.client.get(reverse("survey_delete", args=[survey.slug]))
        assertTemplateUsed(response, "surveys/delete.html")


class TestSurveyEdit:
    client = Client()

    def test_survey_edit_view_url_exists(self, user_factory, survey_factory):
        user = user_factory()
        survey = survey_factory(author=user)
        self.client.force_login(user=user)

        response = self.client.get(f"/my_surveys/{survey.slug}/edit/")
        assert response.status_code == 200

    def test_survey_edit_by_url_name(self, user_factory, survey_factory):
        user = user_factory()
        survey = survey_factory(author=user)
        self.client.force_login(user=user)

        response = self.client.get(reverse("survey_edit", args=[survey.slug]))
        assert response.status_code == 200

    def test_survey_edit_view_template(self, user_factory, survey_factory):
        user = user_factory()
        survey = survey_factory(author=user)
        self.client.force_login(user=user)

        response = self.client.get(reverse("survey_edit", args=[survey.slug]))
        assertTemplateUsed(response, "surveys/edit.html")


class TestSurveyQuestionsEditView:
    client = Client()

    def test_survey_questions_edit_view_url_exists(self, user_factory, survey_factory):
        user = user_factory()
        survey = survey_factory(author=user)
        self.client.force_login(user=user)

        response = self.client.get(f"/my_surveys/{survey.slug}/edit/add_question/")
        assert response.status_code == 200

    def test_survey_questions_edit_url_by_name(self, user_factory, survey_factory):
        user = user_factory()
        survey = survey_factory(author=user)
        self.client.force_login(user=user)

        response = self.client.get(reverse("questions_edit", args=[survey.slug]))
        assert response.status_code == 200

    def test_survey_questions_edit_view_template(self, user_factory, survey_factory):
        user = user_factory()
        survey = survey_factory(author=user)
        self.client.force_login(user=user)

        response = self.client.get(reverse("questions_edit", args=[survey.slug]))
        assertTemplateUsed(response, "surveys/edit_questions.html")


class TestQuestionsOptionsEditView:
    client = Client()

    def test_survey_questions_options_edit_view_url_exists(self, question_factory):
        question = question_factory()
        self.client.force_login(user=question.survey.author)

        response = self.client.get(
            f"/my_surveys/{question.survey.slug}/edit/{question.pk}/add_options/"
        )
        assert response.status_code == 200

    def test_survey_questions_options_edit_view_url_by_name(self, question_factory):
        question = question_factory()
        self.client.force_login(user=question.survey.author)

        response = self.client.get(
            reverse(
                "options_edit", kwargs={"slug": question.survey.slug, "pk": question.pk}
            )
        )
        assert response.status_code == 200

    def test_survey_questions_options_edit_view_template(self, question_factory):
        question = question_factory()
        self.client.force_login(user=question.survey.author)

        response = self.client.get(
            reverse(
                "options_edit", kwargs={"slug": question.survey.slug, "pk": question.pk}
            )
        )
        assertTemplateUsed(response, "surveys/edit_question_options.html")


class TestSurveyAnswerView:
    client = Client()

    def test_survey_answer_view_url_exists(self, user_factory, survey_factory):
        user = user_factory()
        survey = survey_factory(author=user)
        self.client.force_login(user=user)

        response = self.client.get(f"/my_surveys/{survey.slug}/answer/")
        assert response.status_code == 200

    def test_survey_answer_view_url_by_name(self, user_factory, survey_factory):
        user = user_factory()
        survey = survey_factory(author=user)
        self.client.force_login(user=user)

        response = self.client.get(reverse("survey_answer", args=[survey.slug]))
        assert response.status_code == 200

    def test_survey_answer_view_template(self, user_factory, survey_factory):
        user = user_factory()
        survey = survey_factory(author=user)
        self.client.force_login(user=user)

        response = self.client.get(reverse("survey_answer", args=[survey.slug]))
        assertTemplateUsed(response, "surveys/answer.html")

    def test_survey_answer_view_context(self, option_factory):
        option = option_factory()
        survey = option.question.survey
        self.client.force_login(user=survey.author)

        response = self.client.get(reverse("survey_answer", args=[survey.slug]))
        assert response.context[-1]["survey"] == survey


class TestThankYouView:
    client = Client()

    def test_thankyou_page_url_exists(self):
        response = self.client.get("/thank_you/")
        assert response.status_code == 200

    def test_thankyou_page_url_by_name(self):
        response = self.client.get(reverse("thank_you"))
        assert response.status_code == 200

    def test_thankyou_page_template(self):
        response = self.client.get(reverse("thank_you"))
        assertTemplateUsed(response, "surveys/thank_you.html")
