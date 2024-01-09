from django.db.models.signals import post_save
from django.dispatch import receiver
from guardian.shortcuts import assign_perm

from surveys.models import Question, Survey, User


@receiver(post_save, sender=Survey)
def set_survey_permission(sender, instance, created, **kwargs):
    """Add specific survey view, update and delete permissions to the author on survey instance creation"""

    if created:
        assign_perm("view_own_survey", instance.author, instance)
        assign_perm("edit_own_survey", instance.author, instance)
        assign_perm("delete_own_survey", instance.author, instance)


@receiver(post_save, sender=Question)
def set_question_permission(sender, instance, created, **kwargs):
    """Add specific question view, change and delete permission to the author on question instance creation"""
    author = User.objects.get(survey_author__question_survey__id=instance.id)
    if created:
        assign_perm("view_own_question", author, instance)
        assign_perm("edit_own_question", author, instance)
        assign_perm("delete_own_question", author, instance)
