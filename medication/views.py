from django.shortcuts import redirect, render

from django.shortcuts import render

from .models import Medication
# Create your views here.

def medicine_view(request):
    medicine_object = Medication.objects.all()
    context = {
        'medicine_object': medicine_object
    }
    return render(request , 'medicine/medicine_view.html' , context)
# add
def add_medicine_view(request):
    if request.method =="POST":
        medication_code = request.POST.get("medication_code_txt")
        medication_name = request.POST.get("medication_name_txt")
        medication_cost = request.POST.get("medication_cost_txt")
        note = request.POST.get("note_txt")
       
        medication = Medication(
            medication_code = medication_code,
            medication_name = medication_name,
            medication_cost = medication_cost,
            note = note     
        )
        medication.save()
        return redirect('medicine_view')
        
    return render(request , 'medicine/add_medicine_view.html')

# update
def update_medicine_view(request,mid):
    context = {}
    medication = Medication.objects.get(id = mid)
    if request.method =="POST":
        medication_code = request.POST.get("medication_code_txt")
        medication_name = request.POST.get("medication_name_txt")
        medication_cost = request.POST.get("medication_cost_txt")
        note = request.POST.get("note_txt")
       
        
        medication.medication_code = medication_code
        medication.medication_name = medication_name
        medication.medication_cost = medication_cost
        medication.note = note     
        medication.save()
        return redirect('medicine_view')
    context['medication'] = medication
    return render(request , 'medicine/update_medicine_view.html',context)

# delete
def delete_medicine(request, mid):
    medication = Medication.objects.get(id = mid)
    medication.delete()
    return redirect('medicine_view')