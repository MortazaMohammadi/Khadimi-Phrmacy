from django.db import models
# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=150)
    note = models.TextField(max_length=255, blank = True,null=True)

    def __str__(self):
        return self.first_name + " " + self.last_name
    
class Loen(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    amount = models.FloatField()
    note = models.TextField(max_length= 200)
    date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.customer.first_name +' '+str(self.amount)

    