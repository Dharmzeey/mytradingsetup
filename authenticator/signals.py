from django.db.models.signals import post_save
from django.contrib.auth.models import User

from .models import Profile


def createprofile(sender, instance, created, **kwargs):
  if created:
    user = instance
    Profile.objects.create(
      owner=user
    )


post_save.connect(createprofile, sender=User)