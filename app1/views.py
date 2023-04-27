from django.shortcuts import render
from app1.forms import Personsform
from app1.models import Persons
from django.http import HttpResponseRedirect
# Create your views here.

def index(request):
    return render(request,'app1/index.html',{'msg':'This is Index Page'})


def students(request):
    data = ['tabusha','vamsi','srinu','kiran','teja','raju']
    context = {'data':data}
    return render(request,'app1/student.html',context)
    
def form(request):
    form = Personsform()
    if request.method == 'POST':
        form = Personsform(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            age=form.cleaned_data['age']
            gender=form.cleaned_data['gender']
            phno=form.cleaned_data['phno']
            A = Persons(name=name,age=age,gender=gender,phno=phno)
            A.save()
            form = Personsform()    
        else:
            print('notvalid')
    context = {'msg':'this is students page','form':form}
    return render(request,'app1/form.html',context)

def retrieve(request):
    data1 =Persons.objects.all()
    context = {'msg':'this is retrieve page','data1':data1}
    return render(request,'app1/retrieve.html',context)

def update(request,id):
    if request.method == 'POST':
        data2 = Persons.objects.get(pk=id)
        form = Personsform(request.POST,instance=data2)
        if form.is_valid():
            form.save()
    else:
        data2 = Persons.objects.get(pk=id)
        form = Personsform(instance=data2)
    context = {'msg':'updated successfully','form':form}
    return render(request,'app1/update.html',context)

def delete(request,id):
    if request.method == 'POST':
        data2 = Persons.objects.get(pk=id)
        data2.delete()
        return HttpResponseRedirect('/app1/retrieve')




