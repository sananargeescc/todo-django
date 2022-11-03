from django.shortcuts import render, redirect

# Create your views here.
from todoapp.forms import todoform
from todoapp.models import todo


def home(request):

    return render(request,'TODO.html')

def addtodo(request):
    form = todoform()  # form
    todos = todo.objects.all()  # model name

    if request.method=='POST':
        form = todoform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request,'add.html',{'form':form,'todos':todos})
def viewtitle(request):
    data=todo.objects.all()
    return render(request,'view.html',{'data':data})

def update(request,id):
    Todo=todo.objects.get(id=id)
    form=todoform(instance=Todo)
    if request.method == 'POST':
        form = todoform(request.POST,instance=Todo)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request,'update.html',{'form':form,'Todo':Todo})

def delete(request,id):

        todo.objects.get(id=id).delete()
        return redirect('home')



