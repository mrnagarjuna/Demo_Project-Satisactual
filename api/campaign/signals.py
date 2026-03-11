from ..campaign.models import CmpWaves,CmpCampaigns,CmpTeam
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from datetime import timedelta




@receiver(post_save, sender=CmpCampaigns)
def create_wave_for_campaign(sender, instance, created, **kwargs):
    """
    Automatically create a wave when a campaign is created
    """
    if created:

        today = timezone.now().date()
        five_years_later = today + timedelta(days=365 * 5)

        CmpWaves.objects.create(
            id_campaign=instance,
            txt_campaign_wave_name=f"Wave for Campaign {instance.id}",
            dat_wave_start=today,
            dat_wave_end=five_years_later,
            txt_wave_delivery_head_id=instance.created_by  # taking from campaign
        )


@receiver(post_save, sender=CmpCampaigns)
def create_team_for_campaign(sender, instance, created, **kwargs):
    """
    Automatically create team manager when a campaign is created
    """
    if created:

        today = timezone.now().date()
        five_years_later = today + timedelta(days=365 * 5)

        CmpTeam.objects.create(
            id_campaign=instance,
            txt_login_id=instance.created_by,
            txt_campaign_role="Manager",
            dat_joined_team=today,
            dat_left_team=five_years_later,
            created_by=instance.created_by
        )