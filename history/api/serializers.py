from rest_framework import serializers
from ..models import PatientHistory

class PatientHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientHistory
        fields = ['id', 'patient', 'history_of_presenting_illness', 'past_medical_history',
         'medication_history', 'family_history', 'social_history']