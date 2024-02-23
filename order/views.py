from django.shortcuts import redirect, render

from django.shortcuts import render

from .models import *

# Create your views here.

# list
def order_view(request):
    order_object = Order.objects.all()
    costs = []
    for i in order_object:
        t = i.medication.medication_cost * i.quantity
        costs.append(t)
        
    context = {
        'data': zip(order_object,costs)
    }
    
    return render(request , 'order/order_view.html' , context)

# add
def add_order_view(request):
    if request.method == "POST":
        medication = request.POST.get('medication_txt')
        quantity = request.POST.get('quantity_txt')
        customer = request.POST.get('customer_txt')
        date = request.POST.get('date_txt')
        note = request.POST.get('note')
        try:
             m = Medication.objects.get(medication_code = medication)
             c = Customer.objects.get(id = customer)
        except:
            return redirect('add_order_view')
        order = Order(
            medication = m,
            customer = c,
            quantity = quantity,
            date = date,
            note = note
        )
        order.save()
        return redirect('order_view')
    return render(request , 'order/add_order_view.html')

# update
def update_order_view(request,oid):
    context={}
    order = Order.objects.get(id = oid)
    if request.method == "POST":
        medication = request.POST.get('medication_txt')
        quantity = request.POST.get('quantity_txt')
        customer = request.POST.get('customer_txt')
        date = request.POST.get('date_txt')
        note = request.POST.get('note')
        
        
        try:
            order.medication = Medication.objects.get(medication_code = medication)
        except:
            return redirect('update_order_view')
        order.quantity = quantity
        try:
            order.customer = Customer.objects.get(id = customer)
        except:
            return redirect("update_order_view")
        order.date = date
        order.note = note
        
        order.save()
        return redirect('order_view')
    else:
        context['order'] = order
    return render(request , 'order/update_order_view.html',context)

# delete
def delete_order_view(request,oid):
    order = Order.objects.get(id = oid)
    order.delete()
    return redirect('order_view')

