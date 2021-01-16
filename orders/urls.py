from django.urls import path
from .views import OrderView, OrderSubmitView

urlpatterns = [
    path('', OrderView.as_view(), name='order'),
    path('order-submit', OrderSubmitView.as_view(), name='order-submit'),
]