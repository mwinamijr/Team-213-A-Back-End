from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import HistoryListView

urlpatterns = [
    path('patientHistory/', HistoryListView.as_view()),
    path('patientHistory/<int:pk>/', HistoryListView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)