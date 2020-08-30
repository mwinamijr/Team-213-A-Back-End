from django.db import models
from django.contrib.auth.models import User

class PatientHistory(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    history_of_presenting_illness = models.TextField(blank=True)
    past_medical_history = models.TextField(blank=True,
        null=True)
    medication_history = models.TextField(blank=True,
        null=True)
    family_history = models.TextField(blank=True,
        null=True)
    social_history = models.TextField(blank=True,
        null=True)

    def __str__(self):
        return self.patient