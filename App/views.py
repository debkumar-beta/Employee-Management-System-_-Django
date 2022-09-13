from unicodedata import name
from django.shortcuts import render,HttpResponse
from .models import Employee,Role,Department
from datetime import datetime
from django.db.models import Q
# Create your views here.
def index(request):
    return render(request,'index.html')

    
def view_employee(request):
    emps= Employee.objects.all()
    context={
        'emps':emps
    }

    return render(request,'view_employee.html',context)
    
def add_employee(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        dept=int(request.POST['dept'])
        role=int(request.POST['role'])
        salary=int(request.POST['salary'])
        bonus=int(request.POST['bonus'])
        phone=int(request.POST['phone'])
        date=datetime.now()
        data1=Employee(first_name=first_name, last_name=last_name, dept_id=dept, salary=salary, bonus=bonus, role_id=role,phone=phone,hire_date=date)
        data1.save()
        return HttpResponse("The new Employee Details Added!")
    elif request.method=='GET':
        return render(request,'add_employee.html')
    else: 
        return HttpResponse("Error Happens!")



def remove_employee(request,emp_id=0):
    if emp_id:
        try:
            emp_del=Employee.objects.get(id=emp_id)
            emp_del.delete()
            return HttpResponse("Employee Details Succesfully Deleted!")
        except:
            return HttpResponse("Please Select a Employee Properly!!")
    emps=Employee.objects.all()
    
    context={
        'emps':emps
    } 
    return render(request,'remove_employee.html',context)



def filter_employee(request):
    if request.method=='POST':
        name=request.POST['name']
        role=request.POST['role']
        dept=request.POST['dept']
        phone=request.POST['phone']
        emps=Employee.objects.all()
        if name:
            emps=emps.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))    
        if dept:
            emps= emps.filter(dept__name__icontains=dept)
        if role:
            emps=emps.filter(role__name__icontains=role)
        if phone:
            emps=emps.filter(phone=phone)
        context = {
            
            'emps':emps
        }
        
        return render(request,'view_employee.html',context)
    elif request.method=='GET':
        return render(request,'filter_employee.html')    
    else:
        return HttpResponse("Error Happens!")        