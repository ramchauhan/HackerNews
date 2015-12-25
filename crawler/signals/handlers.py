from django.core.management import call_command
from django.contrib.auth.signals import user_logged_in
from django.conf import settings


def crawl_data_and_save_in_db(sender, **kwargs):
    call_command('crawlnews')
