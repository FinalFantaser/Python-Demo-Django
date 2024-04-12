import django.views
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import Customer
from .forms import NewCustomerForm


class Main(django.views.View):
    def get(self, request):
        return render(request=request, template_name='main.html', context={'form': NewCustomerForm()})

class About(django.views.View):
    def get(self, request):
        return render(request=request, template_name='about.html')

class Gallery(django.views.View):
    def get(self, request):
        return render(request=request, template_name='gallery.html', context={'img_indexes': range(1, 13)})


class Book(django.views.View):
    def post(self, request):
        form_data = NewCustomerForm(data=request.POST)

        if form_data.is_valid():
            new_customer = Customer(name=request.POST['name'], phone=request.POST['phone'])
            new_customer.save()

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
