from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Employee
# Create your views here.


def first(request):
    employee = Employee.objects.all()
    return render(request, 'OOfirst.html', {'employee': employee})


def add(request):
    return render(request, 'add.html')


def success(request):
    iid = request.POST.get('eid', 'default')
    iname = request.POST.get('ename', 'default')
    iemail = request.POST.get('eemail', 'default')
    icontact = request.POST.get('econtact', 'default')
    employee = Employee(eid=iid, ename=iname, eemail=iemail, econtact=icontact)

    employee.save()

    return HttpResponse('<h1> Saved Successfully !!!<br><a href="/myapp">Back To Myapp </a></h1>')


def edit(request, id):
    employee = Employee.objects.get(id=id)
    return render(request, 'edit.html', {'employee': employee})


def update(request, id):
    employee = Employee.objects.get(id=id)
    iid = request.POST.get('eid', 'default')
    iname = request.POST.get('ename', 'default')
    iemail = request.POST.get('eemail', 'default')
    icontact = request.POST.get('econtact', 'default')

    employee.eid = iid
    employee.ename = iname
    employee.eemail = iemail
    employee.econtact = icontact

    employee.save()

    return HttpResponse('<h1> Updated Successfully !!!<br><a href="/myapp">Back To Myapp </a></h1>')


def delete(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return HttpResponse('<h1> Record Deleted Successfully !!!<br><a href="/myapp">Back To Myapp </a></h1>')