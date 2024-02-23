from django.contrib import admin

# Register your models here.

from .models  import Customer
# Register your models here.

class CustomerAdmin(admin.ModelAdmin):

    list_display = ['first_name', 'last_name', 'phone']

    class Meta:
        models = Customer

admin.site.register(Customer,CustomerAdmin)