from django.conf.urls import *
from rest_framework import routers

from .views import FinanceDataViewSet
from .views import FinanceDataView

router = routers.DefaultRouter()
router.register(r'financedata', FinanceDataViewSet)

urlpatterns = [
    url(r'^finance/$', FinanceDataView.as_view(), name='finance'),
    url(r'^api/v1/', include(router.urls)),
]