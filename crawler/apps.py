from django.apps import AppConfig


class CrawlerConfig(AppConfig):
    name = 'crawler'
    verbose_name = "Crawler"

    def ready(self):
        import crawler.signals.handlers
