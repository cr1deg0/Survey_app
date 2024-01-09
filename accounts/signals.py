from django.contrib.auth.models import Permission, User
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def set_user_permission(sender, instance, created, **kwargs):
    """Add general survey CRUD permissions to the user"""
    if created:
        instance.user_permissions.add(Permission.objects.get(name="Can add survey"))
        instance.user_permissions.add(Permission.objects.get(name="Can change survey"))
        instance.user_permissions.add(Permission.objects.get(name="Can delete survey"))
        instance.user_permissions.add(Permission.objects.get(name="Can view survey"))
