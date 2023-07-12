from django.shortcuts import render
from .models import Finch
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    finches = Finch.objects.all()
    return render(request, 'finches/index.html', {
        'finches':finches
    })

def finches_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    return render(request, 'finches/details.html', {
        'finch' : finch
    })

# class FinchCreate(CreateView):
#     model = Finch
#     fields = ['name', 'color', 'age', 'description']
#     template_name = 'main_app/finch_form.html'

class FinchCreate(CreateView):
    model = Finch
    fields = ['name', 'color', 'age', 'description']
    template_name = 'main_app/finch_form.html'

class FinchUpdate(UpdateView):
    model = Finch
    fields = ['name', 'color', 'age', 'description']

class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finches' 