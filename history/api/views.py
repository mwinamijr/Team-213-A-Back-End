from ..models import PatientHistory
from .serializers import PatientHistorySerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class HistoryListView(APIView):
    """
    List all patient's history, or create a new patient's history.
    """
    def get(self, request, format=None):
        history = PatientHistory.objects.all()
        serializer = PatientHistorySerializer(history, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PatientHistorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)