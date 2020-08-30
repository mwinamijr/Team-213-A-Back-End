from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import HistoryListView, HistoryDetail

urlpatterns = [
    path('patientHistory/', HistoryListView.as_view(), name='history'),
    path('patientHistory/<int:pk>/', HistoryDetail.as_view(), name='history-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)