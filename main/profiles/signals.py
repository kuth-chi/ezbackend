from django.dispatch import receiver
from models import Profile
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# Create User instance Profile object
@receiver(post_save, sender=User)
def create_profile(self, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)