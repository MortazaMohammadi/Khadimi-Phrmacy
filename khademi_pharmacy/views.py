from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models.functions import TruncWeek , TruncDay , TruncMonth
from django.db.models import Sum


from medication.models import Medication
from customer.models import *
from order.models import *


@login_required(login_url='/')
def home_page(request):
    context = {}
    last_day_income = Order.objects.annotate(day=TruncDay('date')).values('day').annotate(
    total_income=Sum('quantity') * Sum('medication__medication_cost')).order_by('-day').first()
    
    last_week_income = Order.objects.annotate(week=TruncWeek('date')).values('week').annotate(
    total_income=Sum('quantity') * Sum('medication__medication_cost')).order_by('-week').first()
    
    last_month_income = Order.objects.annotate(month=TruncMonth('date')).values('month').annotate(
    total_income=Sum('quantity') * Sum('medication__medication_cost')).order_by('-month').first()

    order_total = Order.objects.all().count()
    medicine_total = Medication.objects.all().count()
    customer_total = Customer.objects.all().count()
    loen_total = Loen.objects.aggregate(total_amount=Sum('amount'))['total_amount']

    context['last_day_income'] = last_day_income['total_income']
    context['last_week_income'] = last_week_income['total_income'] // 2
    context['last_month_income'] = last_month_income['total_income'] // 2
    print(loen_total)
    context['order_total'] = order_total
    context['medicine_total'] = medicine_total
    context['loen_total'] = loen_total
   
    context['customer_total'] = customer_total

    total_income = 0

    prescription_item_object = Order.objects.all()

    for item in prescription_item_object:
        total_income += item.quantity * item.medication.medication_cost

    context['total_income'] = total_income
    
    return render(request , 'home.html' , context)