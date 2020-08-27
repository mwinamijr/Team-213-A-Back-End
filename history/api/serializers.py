from ..models import PatientHistory

class PatientHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientHistory
        fields = ['id', 'patient', '']