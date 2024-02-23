from django.db import models

# Create your models here.

class Medication(models.Model):
    medication_code = models.CharField(max_length=200)
    medication_name = models.CharField(max_length=200)
    medication_cost = models.FloatField()
    note = models.TextField(max_length = 200, blank = True, null= True)

    def __str__(self):
        return self.medication_name