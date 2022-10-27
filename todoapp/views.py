from django.shortcuts import render, redirect

# Create your views here.
from todoapp.forms import todoform
from todoapp.models import todo


def home(request):
    form = todoform()   # form
    todos = todo.objects.all()  # model name
    if request.method == 'POST':
        form = todoform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request,'TODO.html',{'form':form,'todos':todos})

