from django.apps import AppConfig


class PermisAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'permis_app'
    def ready(self):
        import permis_app.signals