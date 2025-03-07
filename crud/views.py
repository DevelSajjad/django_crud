from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User
import pprint
def add_show(request):
    if request.method ==  'POST':
        form = StudentRegistration(request.POST)
        if form.is_valid():
            userSaveData = User(
                name= form.cleaned_data['name'],
                email= form.cleaned_data['email'],
                password= form.cleaned_data['password']
            )
            userSaveData.save()
            form = StudentRegistration()
    else:
        form = StudentRegistration()
    students = User.objects.all()
    return render(request, 'crud/add_and_show.html', {'form': form, 'students': students})

def deleteStudent(request, id):
    student = User.objects.get(pk=id)
    if student:
        student.delete()
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')

def studentUpdate(request, id):
    student = User.objects.get(pk=id)
    if request.method == 'POST':
      form = StudentRegistration(request.POST, instance=student)
      if form.is_valid():
        student.name = form.cleaned_data['name'],
        student.email = form.cleaned_data['email'],
        student.password = form.cleaned_data['password']
        student.save()
        return HttpResponseRedirect('/')
    else:
        
        form = StudentRegistration(instance=student)
        return render(request, 'crud/student_update.html', {'form': form})


