from django.core.management import call_command
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver


@receiver(user_logged_in)
def crawl_data_and_save_in_db(sender, **kwargs):
    """
    signal to call the management command for crawl the data and then save the data in DB
    :param sender:
    :param kwargs:
    :return:
    """
    call_command('crawlnews', **kwargs)
