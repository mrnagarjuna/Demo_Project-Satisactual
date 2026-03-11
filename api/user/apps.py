from django.apps import AppConfig

class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api.user'

    def ready(self):
        # Import signals so that they are registered
        import api.user.signals
