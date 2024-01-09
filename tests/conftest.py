from pytest_factoryboy import register

from .factories import OptionFactory, QuestionFactory, SurveyFactory, UserFactory

register(UserFactory)
register(SurveyFactory)
register(QuestionFactory)
register(OptionFactory)
