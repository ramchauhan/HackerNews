from django.db import models
from django.contrib.auth.models import User


class NewsItem(models.Model):
    """
    Model for News which needs to be crawl
    """
    title = models.CharField(max_length=255)
    hacker_news_url = models.URLField(max_length=255, unique=True)
    url = models.URLField(max_length=255)
    posted_on = models.DateTimeField()
    upvotes = models.IntegerField()
    comments = models.IntegerField()
    deleted_items = models.ManyToManyField(User, related_name='deleted_items')
    read_items = models.ManyToManyField(User, related_name='read_items')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title
