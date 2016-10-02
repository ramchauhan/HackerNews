from .models import NewsItem
from django.db import transaction


@transaction.atomic
def save_updates(news_items=None):
    """
    Create or Update the records in DB
    :param news_items:
    :return:
    """
    for news in news_items:
        news.update({'deleted_item': False, "read_item": False})
        NewsItem.objects.update_or_create(hacker_news_url=news['hacker_news_url'], defaults=news)