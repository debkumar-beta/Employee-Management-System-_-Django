from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('view_employee',views.view_employee,name="view_employee"),
    path('add_employee',views.add_employee,name="add_employee"),
    path('remove_employee',views.remove_employee,name="remove_employee"),
    path('remove_employee/<int:emp_id>',views.remove_employee,name="remove_employee"),

    path('filter_employee',views.filter_employee,name="filter_employee"),    
]
