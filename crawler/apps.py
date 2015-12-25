from django.apps import AppConfig


class CrawlerConfig(AppConfig):
    """
    app configuration to register the signal
    """
    name = 'crawler'
    verbose_name = "Crawler"

    def ready(self):
        import crawler.signals.handlers
