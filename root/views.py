from django.shortcuts import render
from django.views.generic import DeleteView
from django.http import HttpResponse
from config.models import *
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from .forms import ContactForm


# Create your views here.
def new_url_view(request):
    return HttpResponse("Yangi URL page")


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product_delete.html'
    success_url = '/'


class ContactFormView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = '/'

    def form_valid(self, form):
        return super().form_valid(form)