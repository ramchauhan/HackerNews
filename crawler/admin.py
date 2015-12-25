from django.contrib import admin

from .models import NewsItem


class NewsItemAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    list_display = ["title", "hacker_news_url", "url", "posted_on", "upvotes", "comments",
                    "created_date", "modified_date"]

admin.site.register(NewsItem, NewsItemAdmin)
