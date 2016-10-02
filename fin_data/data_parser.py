import os
from os.path import isfile, join
import xlrd

from django.conf import settings


class FinDataParser(object):
    """
    class to parse the file from a location and make the dict
    """
    def __init__(self, path):
        self.path = path
        self.offset = 1  # this is used to exclude the headers
        self.data_list_dict = []  # this will contains the all file data dict as list of dict

    @property
    def get_files(self):
        """
        this method will get the all file which are having extension as xlsx
        :return:
            list of all files
        """
        return [f for f in os.listdir(self.path) if isfile(join(self.path, f)) and f.split('.')[-1] == 'xlsx']

    def process_files(self):
        """
        this method will process the files
        :return:
        """
        all_files = self.get_files
        for file_name in all_files:
            data_dict = self._parse_data_from_file(file_name)
            self.data_list_dict.extend(data_dict)
        return self.data_list_dict

    def _parse_data_from_file(self, file_name):
        """
        this method will parse the excel file and make the dict
        :param
            file_path (file): file which need to be parsed
        :return:
            data (dict): all dict of data with key
        """
        file_path = os.path.join(self.path, file_name)
        data_file = xlrd.open_workbook(file_path)
        worksheet = data_file.sheet_by_index(0)
        fin_data = []
        for row in xrange(self.offset, worksheet.nrows):
            row_data = worksheet.row(row)
            fin_data.append({
                'stock_date': xlrd.xldate.xldate_as_datetime(row_data[0].value, data_file.datemode).utcnow(),
                'stock_open_price': row_data[1].value,
                'stock_high_price': row_data[2].value,
                'stock_low_price': row_data[3].value,
                'stock_close_price': row_data[4].value,
                'stock_volume': row_data[5].value,
                'stock_adj_close': row_data[6].value,
                'stock_id': int(row_data[7].value)
            })
        return fin_data
