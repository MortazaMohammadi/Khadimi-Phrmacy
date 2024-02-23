from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('medicine_view' , medicine_view , name="medicine_view"),
    path('add_medicine_view' , add_medicine_view , name="add_medicine_view"),
    path('update_medicine_view/<int:mid>',update_medicine_view,name="update_medicine_view"),
    path('delete_medicine/<int:mid>', delete_medicine, name="medicine")
]