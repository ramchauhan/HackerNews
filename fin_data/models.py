from django.db import models


class FinanceDataId(models.Model):
    """
    model for Finance data ID
    """
    stock_id = models.IntegerField(primary_key=True)

    class Meta:
        app_label = 'fin_data'

    def __unicode__(self):
        return str(self.stock_id)


class FinanceDataItem(models.Model):
    """
    Model for FinanceData Items
    """
    stock = models.ForeignKey(FinanceDataId)
    stock_date = models.DateTimeField(unique=True)
    stock_open_price = models.FloatField()
    stock_high_price = models.FloatField()
    stock_low_price = models.FloatField()
    stock_close_price = models.FloatField()
    stock_volume = models.FloatField()
    stock_adj_close = models.FloatField()

    class Meta:
        app_label = 'fin_data'

    def __unicode__(self):
        return str(self.stock)
