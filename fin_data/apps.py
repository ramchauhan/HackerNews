from django.apps import AppConfig


class FinDataConfig(AppConfig):
    name = 'fin_data'
    verbose_name = "Fin_data"

    def ready(self):
        import fin_data.signals.handlers
