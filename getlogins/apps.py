from django.apps import AppConfig


class GetloginsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'getlogins'

    def ready(self):
        import getlogins.signals 