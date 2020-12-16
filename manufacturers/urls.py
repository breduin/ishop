from django.urls import path
from .views import ManufacturersListView, ManufacturerDetailView

urlpatterns = [
    path('', ManufacturersListView.as_view(), name='manufacturers'),
    path('<str:slug>/', ManufacturerDetailView.as_view(), name='manufacturer'),
]