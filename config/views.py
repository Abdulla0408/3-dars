from django.shortcuts import render
from .models import *
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.http import HttpResponse


class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')

    def post(self, request):
        return render(request, 'home.html')


class ProductListView(ListView):
    model = Product
    template_name ='products_list.html'
    context_object_name = 'products'

class CategoryDetailView(ListView):
    model = Category
    template_name ='category_detail.html'
    context_object_name = 'category'


class ProductAddView(CreateView):
    model = Product
    template_name = 'product_add.html'
    fields = ('name', 'quantity', 'price', 'category', 'description')
    success_url = '/'

