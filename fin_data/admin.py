from django.contrib import admin

from .models import FinanceDataItem, FinanceDataId


class MultiDBModelAdmin(admin.ModelAdmin):
    # A handy constant for the name of the alternate database.
    using = 'fin_data'

    def save_model(self, request, obj, form, change):
        # Tell Django to save objects to the 'other' database.
        obj.save(using=self.using)

    def delete_model(self, request, obj):
        # Tell Django to delete objects from the 'other' database
        obj.delete(using=self.using)

    def get_queryset(self, request):
        # Tell Django to look for objects on the 'other' database.
        return super(MultiDBModelAdmin, self).get_queryset(request).using(self.using)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        # Tell Django to populate ForeignKey widgets using a query
        # on the 'other' database.
        return super(MultiDBModelAdmin, self).formfield_for_foreignkey(db_field, request, using=self.using, **kwargs)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        # Tell Django to populate ManyToMany widgets using a query
        # on the 'other' database.
        return super(MultiDBModelAdmin, self).formfield_for_manytomany(db_field, request, using=self.using, **kwargs)


class FinanceDataIdAdmin(admin.ModelAdmin):
    search_fields = ["stock_id"]
    list_display = ["stock_id"]


class FinanceDataAdmin(admin.ModelAdmin):
    """
    class for adding finance data into admin section
    """
    search_fields = ["stock"]
    readonly_fields = ("stock_open_price", "stock_close_price", "stock", "stock_adj_close",
                       "stock_volume", "stock_volume", "stock_low_price", "stock_high_price", "stock_date")

    list_display = ["stock_open_price", "stock_close_price", "stock", "stock_adj_close",
                    "stock_volume", "stock_volume", "stock_low_price", "stock_high_price", "stock_date"]


admin.site.register(FinanceDataItem, FinanceDataAdmin)
admin.site.register(FinanceDataId, FinanceDataIdAdmin)
# othersite = admin.AdminSite('othersite')
# othersite.register(FinanceDataItem, FinanceDataAdmin)
