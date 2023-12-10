from venv import create
from django.db.models.signals import post_save
from django.dispatch import receiver
from guardian.shortcuts import assign_perm
from surveys.models import Survey, Question, User


@receiver(post_save, sender=Survey)
def set_survey_permission(sender, instance, created, **kwargs):
    """ Add view and change survey permissions to the author on instance creation """
    print(f'{instance} created {created}')
    if created:
        assign_perm(
            "view_own_survey",
            instance.author,
            instance
        )
        assign_perm(
            "edit_own_survey",
            instance.author,
            instance
        )

@receiver(post_save, sender=Question)
def set_question_permission(sender, instance, created, **kwargs):
    """ Add change question permission to the author on instance creation """
    print(f'{instance} created {created}')
    print(instance.__dict__)
    author = User.objects.get(survey_author__question_survey__id=instance.id)
    print(author)
    if created:
        assign_perm(
            "view_own_question",
            author,
            instance
        )
        assign_perm(
            "edit_own_question",
            author,
            instance
        )