import logging
from datetime import datetime
from django.conf import settings
from django.core.management.base import BaseCommand

from ...data_parser import FinDataParser
from ...utils import save_updates

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    """
    Command to crawl the HackersNews and Update the data in DB
    This command will not work by using command line
    """
    def handle(self, *args, **options):
        """
        command handler
        :param args:
        :param options:
        :return:
        """
        try:
            options['request'].user.id
        except KeyError:
            raise Exception("You are not authorised to do this.")

        all_data = self.get_fin_data
        save_updates(all_data)

    @property
    def get_fin_data(self):
        """
        get the all finance data
        :return:
        """
        fin_parser = FinDataParser(settings.FIN_DATA_FILE_LOC)
        fin_data = fin_parser.process_files()
        return fin_data
