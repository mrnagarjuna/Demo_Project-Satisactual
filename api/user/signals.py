from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import SecUserMaster, SecUserPreferences

@receiver(post_save, sender=SecUserMaster)
def create_user_preferences(sender, instance, created, **kwargs):
    """
    Automatically create SecUserPreferences for every new SecUserMaster.
    """
    if created:
        SecUserPreferences.objects.create(txt_login_id=instance)


@receiver(post_save, sender=SecUserMaster)
def save_user_preferences(sender, instance, **kwargs):
    """
    Ensure that the user's preferences are saved when the user is saved.
    """
    try:
        instance.profile.save()
    except SecUserPreferences.DoesNotExist:
        # If somehow preferences were deleted, recreate them
        SecUserPreferences.objects.create(txt_login_id=instance)
