from collections import OrderedDict
from django.conf import settings
from django.views.generic import TemplateView
from django.views.generic import ListView
from rest_framework.response import Response
from rest_framework import viewsets

from .models import FinanceDataItem, FinanceDataId
from .serializers import FinanceDataSerializer


class FinanceDataListView(ListView):
    """
    Finance Data View to display the all Finanance Data
    """
    model = FinanceDataItem
    context_object_name = 'fin_data_items'
    template_name = 'fin_base.html'

    def get_queryset(self):
        return self.model.objects.all()


class FinanceDataViewSet(viewsets.ModelViewSet):
    """
    FinanceDataSerializer Viewset
    """
    queryset = FinanceDataItem.objects.all()
    serializer_class = FinanceDataSerializer

    def list(self, request, *args, **kwargs):
        fin_ids = FinanceDataId.objects.all()
        response_data = OrderedDict()
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        all_data = serializer.data
        for obj in fin_ids:
            filtered_data = [data for data in all_data if data['stock'] == obj.stock_id]
            if filtered_data:
                response_data.update({obj.stock_id: filtered_data})
        return Response(data=response_data)


class FinanceDataView(TemplateView):
    template_name = 'fin_base.html'

    def get_context_data(self, **kwargs):
        context = super(FinanceDataView, self).get_context_data(**kwargs)
        context.update({'STATIC_URL': settings.STATIC_URL})
        context.update({'END_POINT': settings.API_END_POINT})
        return context


