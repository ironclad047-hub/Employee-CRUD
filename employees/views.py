from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Employee

# Список всех
class EmployeeList(ListView):
    model = Employee
    template_name = 'index.html'
    context_object_name = 'employees'

# Создание
class EmployeeCreate(CreateView):
    model = Employee
    fields = ['full_name', 'position', 'email', 'photo']
    template_name = 'form.html'
    success_url = reverse_lazy('list')

# Редактирование
class EmployeeUpdate(UpdateView):
    model = Employee
    fields = ['full_name', 'position', 'email', 'photo']
    template_name = 'form.html'
    success_url = reverse_lazy('list')

# Удаление
class EmployeeDelete(DeleteView):
    model = Employee
    template_name = 'confirm.html'
    success_url = reverse_lazy('list')
