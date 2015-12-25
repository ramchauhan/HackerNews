from django.views.generic import ListView
from .models import NewsItem
from django.contrib.auth.signals import user_logged_in
from signals.handlers import crawl_data_and_save_in_db
from django.conf import settings


class NewsItemListView(ListView):
    model = NewsItem
    context_object_name = 'news_items'
    ordering = '-id'

    def get_queryset(self):
        user_logged_in.connect(crawl_data_and_save_in_db, sender=settings.AUTH_USER_MODEL)
        return NewsItem.objects.exclude(id__in=self.request.user.deleted_items.all()).order_by(self.ordering)