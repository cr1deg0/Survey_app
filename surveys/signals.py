from venv import create
from django.db.models.signals import post_save
from django.dispatch import receiver
from guardian.shortcuts import assign_perm
from surveys.models import Survey


@receiver(post_save, sender=Survey)
def set_survey_permission(sender, instance, created, **kwargs):
    """ Add view, change and delete survey permission to the author """
    print(f'{instance} created {created}')
    if created:
        assign_perm(
            "view_own_survey",
            instance.author,
            instance
        )
