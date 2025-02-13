from django.apps import AppConfig


class WorkshopConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "TheGuild.core"

    def ready(self):
        print("Core setup")
