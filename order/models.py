from django.db import models

from customer.models import Customer

from medication.models import Medication
# Create your models here.

class Order(models.Model):
    medication = models.ForeignKey(Medication , on_delete=models.CASCADE)
    quantity = models.IntegerField()
    note = models.TextField(blank=True , null = True , default='Sold for cost')
    customer = models.ForeignKey(Customer, blank=True, null = True , on_delete=models.SET_NULL)
    date = models.DateField()
    def __str__ (self):
        return str(self.quantity) + str(self.quantity)