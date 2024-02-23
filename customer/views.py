from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Customer, Loen
# Create your views here.
@login_required(login_url='/')
def customer_view(request):
    customer_object = Customer.objects.all()
    context = {
        'customer_object': customer_object
    }
    return render(request , 'customer/customer_view.html' , context)

@login_required(login_url='/')
def add_customer_view(request):
    
    if request.method == "POST":
        first_name = request.POST.get('first_name_txt')
        last_name = request.POST.get('last_name_txt')
        phone = request.POST.get('phone_txt')
        address = request.POST.get('address_txt')
        note = request.POST.get('note_txt')
        
        customer = Customer(
            first_name = first_name,
            last_name = last_name,
            phone = phone,
            address = address,
            note = note
        )
        customer.save()
        return redirect('customer_view')
    return render(request,'customer/add_customer_view.html')

# update
@login_required(login_url='/')
def update_customer_view(request, cid):
    context={}
    customer = Customer.objects.get(id =cid)
    if request.method == "POST":
        first_name = request.POST.get('first_name_txt')
        last_name = request.POST.get('last_name_txt')
        phone = request.POST.get('phone_txt')
        address = request.POST.get('address_txt')
        note = request.POST.get('note_txt')
        
        
        customer.first_name = first_name
        customer.last_name = last_name
        customer.phone = phone
        customer.address = address
        customer.note = note
        
        customer.save()
        return redirect('customer_view')
    else:
        context['customer'] = customer
    return render(request,'customer/update_customer_view.html',context)

@login_required(login_url='/')
def delete_customer(request,cid):
    Customer.objects.get(id =cid).delete()
    return redirect('customer_view')
    
@login_required(login_url='/')
def loen_view(request):
    context= {}
    loen = Loen.objects.all()
    context['loen'] = loen
    return render(request, 'customer/loen_view.html',context)
@login_required(login_url='/')
def add_loen_view(request):
    if request.method == "POST":
        customer = request.POST.get('customer_txt')
        amount = request.POST.get('amount_txt')
        note = request.POST.get('note_txt')
        try:
           c= Customer.objects.get(id = customer)
        except:
            return redirect('add_loen_view')
        loen = Loen(
            customer = c,
            amount = amount,
            note = note,
        )
        loen.save()
        return redirect('loen_view')
    return render(request, 'customer/add_loen_view.html')
@login_required(login_url='/')
def update_loen_view(request,lid):
    context={}
    loen = Loen.objects.get(id = lid)
    
    if request.method == "POST":
        customer = request.POST.get('customer_txt')
        amount = request.POST.get('amount_txt')
        note = request.POST.get('note_txt')
        try:
           c= Customer.objects.get(id = customer)
        except:
            return redirect('update_loen_view/'+str(lid))
        
        loen.customer = c
        loen.amount = amount
        loen.note = note
        
        loen.save()
        return redirect('loen_view')
    else:
        context['loen'] = loen
    return render(request, 'customer/update_loen_view.html',context)
@login_required(login_url='/')
def delete_loen(request,lid):
    loen = Loen.objects.get(id = lid)
    loen.delete()
    return redirect('loen_view')