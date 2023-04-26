from django.urls import path
from .views import CellList, CellDetail

cell_urlpatterns = [
    path('cells/', CellList.as_view(), name='cell_list'),
    path('cells/<int:pk>/', CellDetail.as_view(), name='cell_detail')
]