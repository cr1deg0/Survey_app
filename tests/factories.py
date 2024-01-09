import factory
from django.contrib.auth.models import User
from pytest_factoryboy import register
from surveys.models import Option, Question, Survey


@register
class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = "user1"


@register
class SurveyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Survey

    title = "survey1"
    author = factory.SubFactory(UserFactory)


@register
class QuestionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Question

    question = "question1"
    survey = factory.SubFactory(SurveyFactory)


@register
class OptionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Option

    option = "option1"
    question = factory.SubFactory(QuestionFactory)
