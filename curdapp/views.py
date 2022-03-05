from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentForm
from .models import User
# Create your views here.
# def add_show(request):
#     return render(request,"addandshow.html")

def add(request):
    if request.method == 'POST':
        fm = StudentForm(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pas = fm.cleaned_data['password']
            reg = User(name=nm,email=em,password=pas)
            # fm.save()
            reg.save()
            fm = StudentForm()
    else:
        fm = StudentForm()
    stud = User.objects.all()
    return render(request,"addandshow.html",{'form':fm,'stu':stud})

def update(request,id):
    if request.method == "POST":
        pi = User.objects.get(pk=id)
        fm = StudentForm(request.POST,instance=pi)
        if fm.is_valid():
           fm.save()
    else :
        pi = User.objects.get(pk=id)
        fm = StudentForm(instance=pi)
    return render(request,'update.html',{'form':fm})





def delete(request,id):
    if request.method == "POST":
        pk = User.objects.get(pk=id)
        pk.delete()
        return HttpResponseRedirect('/')