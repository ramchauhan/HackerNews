from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction

from .models import FinanceDataItem, FinanceDataId


@transaction.atomic
def save_updates(fin_data=None):
    """
    Create or Update the records in DB
    :param fin_data:
    :return:
    """
    for data in fin_data:
        try:
            FinanceDataId.objects.get(stock_id=data['stock_id'])
        except ObjectDoesNotExist:
            fin_data_id_obj = FinanceDataId(stock_id=data['stock_id'])
            fin_data_id_obj.save()
        FinanceDataItem.objects.update_or_create(stock_date=data['stock_date'], defaults=data)
