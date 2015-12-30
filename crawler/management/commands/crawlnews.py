from datetime import timedelta, datetime
import logging
import urllib2
from lxml import html
from django.conf import settings
from django.core.management.base import BaseCommand
from ...utils import save_updates
from ...models import UserProfile

logger = logging.getLogger(__name__)

TIME_UNITS = {
    ('second', 'seconds'): 'seconds',
    ('minute', 'minutes'): 'minutes',
    ('hour', 'hours'): 'hours',
    ('day', 'days'): 'days',
    ('week', 'weeks'): 'weeks'
}


class Command(BaseCommand):
    """
    Command to crawl the HackersNews and Update the data in DB
    This command will not work by using command line
    """
    def crawl_page(self):
        """
        this method returns the data of first three pagination of the hackers news
        :return:
        """
        for page in xrange(1, settings.PAGE_COUNT_LIMIT):
            page = urllib2.urlopen(settings.URL_TO_CRAWL + '?P={}'.format(page))
            yield page

    def handle(self, *args, **options):
        """
        command handler
        :param args:
        :param options:
        :return:
        """
        try:
            user_id = options['request'].user.id
        except KeyError:
            # Here if user trying to run this command with command line then setting the random user by default
            # from existing user
            user = UserProfile.objects.filter(is_superuser=True)
            if user:
                user_id = user[0].id
            else:
                raise Exception("First Create a superuser, then run the command.")
        news_list = []
        for page in self.crawl_page():
            page_content = page.read()
            tree = html.fromstring(page_content)
            all_news = tree.find_class('athing')
            for news_item in all_news:
                try:
                    news_item_dict = self.get_news_data(news_item)
                    news_item_dict.update({'user_name_id': user_id})
                    news_list.append(news_item_dict)
                except IndexError as ex:
                    logger.log(level=logging.ERROR, msg='{0}'.format(ex))
        save_updates(news_list)

    def get_news_data(self, news_item):
        """
        method to parse the crawled data and get the specific fields and make a dict of keys value pair
        :param news_item:
        :return:
        """
        link_tag = news_item.find_class('deadmark')[0].getnext()
        news_url = link_tag.attrib['href']
        if news_url.startswith('item?'):
            news_url = settings.NEWS_COMMENT_URL + '{}'.format(news_url)
        news_title = link_tag.text
        # Here finding the next tr tag to get other require information
        next_tag = news_item.getnext()
        up_votes = int(next_tag.find_class('score')[0].text.split(' ')[0])
        subtext_tags = next_tag.find_class('subtext')[0].getchildren()
        comment_tag = subtext_tags[-1]
        comment_text = comment_tag.text
        if comment_text == 'discuss':
            comment_count = 0
        else:
            comment_count = int(comment_text.split(' ')[0])
        hacker_news_url = settings.NEWS_COMMENT_URL + '{}'.format(comment_tag.attrib['href'])
        post_time_human_readable = subtext_tags[-2].getchildren()[0].text
        post_time_data = post_time_human_readable.split(' ')
        time_value, time_unit = int(post_time_data[0]), post_time_data[1]
        post_time = self.calculate_time(time_value, time_unit)
        return {
            'url': news_url,
            'hacker_news_url': hacker_news_url,
            'posted_on': post_time,
            'upvotes': up_votes,
            'comments': comment_count,
            'title': news_title
        }

    def calculate_time(self, magnitude, unit):
        """
        method to calculate the exact time from human readable time
        :param magnitude:
        :param unit:
        :return:
        """
        key_find = lambda x: [k for k in TIME_UNITS if x in k]
        time_key = key_find(unit)[0]
        time_unit = TIME_UNITS[time_key]
        return datetime.now()-timedelta(**{time_unit: magnitude})
