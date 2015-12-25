import urllib2
import logging
from datetime import timedelta, datetime
from lxml import html
from django.core.management.base import BaseCommand
from django.conf import settings
from ...utils import save_updates

logger = logging.getLogger(__name__)

TIME_UNITS = {
    ('second', 'seconds'): 'seconds',
    ('minute', 'minutes'): 'minutes',
    ('hour', 'hours'): 'hours',
    ('day', 'days'): 'days',
    ('week', 'weeks'): 'weeks'
}


class Command(BaseCommand):
    import pdb; pdb.set_trace()
    help = 'used to get the data when running the command'

    def crawl_page(self):
        for page in xrange(1, settings.PAGE_COUNT_LIMIT):
            page = urllib2.urlopen(settings.URL_TO_CRAWL + '?P={}'.format(page))
            yield page

    def handle(self, *args, **options):
        news_list = []
        for page in self.crawl_page():
            page_content = page.read()
            tree = html.fromstring(page_content)
            all_news = tree.find_class('athing')
            for news_item in  all_news:
                try:
                    news_list.append(self.get_news_data(news_item))
                except IndexError as ex:
                    logger.log(level=logging.ERROR, msg='{0}'.format(ex))
        save_updates(news_list)

    def get_news_data(self, news_item):
        link_tag = news_item.find_class('deadmark')[0].getnext()
        news_url = link_tag.attrib['href']
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
        post_time_human_readable = subtext_tags[-2].text
        post_time_data = post_time_human_readable.split(' ')
        time_value, time_unit = int(post_time_data[0]), post_time_data[1]
        # Here i need to understand
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
        key_find = lambda x: [k for k in TIME_UNITS if x in k]
        time_key = key_find(unit)[0]
        time_unit = TIME_UNITS[time_key]
        return datetime.now()-timedelta(**{time_unit: magnitude})