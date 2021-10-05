from django.shortcuts import render
from django.http import HttpResponse
from .models import EmployeeModel
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import (
ListView,
CreateView,
UpdateView,
DeleteView,
)

# Create your views here.
def index(request):
    data = {
        'employees_list': EmployeeModel.objects.all()
        }
    return render(request, 'home.html', data)

class PostCreateView(CreateView):
    model = EmployeeModel
    template_name = 'post_form.html'
    fields = '__all__'

class PostUpdateView(UserPassesTestMixin,UpdateView):
    model = EmployeeModel
    template_name = 'post_form.html'
    fields = '__all__'
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        return True  

class PostDeleteView(UserPassesTestMixin , DeleteView):
    model = EmployeeModel
    template_name = 'post_confirm_delete.html'
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        return True   