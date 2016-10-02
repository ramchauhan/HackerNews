from rest_framework import serializers


from .models import FinanceDataItem


class FinanceDataSerializer(serializers.ModelSerializer):
    """
    FinanceData Serializer
    """
    class Meta:
        model = FinanceDataItem
        fields = ('stock', 'stock_date', 'stock_open_price', 'stock_high_price', 'stock_low_price',
                  'stock_close_price', 'stock_volume', 'stock_adj_close')
