from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api.users'

    def ready(self):
        try:
            from . import signals
        except Exception:
            print("Field to import apps.users.signals.")
        