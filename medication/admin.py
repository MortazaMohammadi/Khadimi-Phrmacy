from django.contrib import admin

# Register your models here.

from .models import Medication

class MedicationAdmin(admin.ModelAdmin):

    list_display = ['medication_code' , 'medication_name' , 'medication_cost']

    class Meta:
        models = Medication

admin.site.register(Medication,MedicationAdmin)