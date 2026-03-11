from django.apps import AppConfig


class CampaignConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api.campaign'

    def ready(self):
        # Import signals so that they are registered
        import api.campaign.signals

