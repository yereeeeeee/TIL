from django.shortcuts import render, redirect
from .models import Store, Product

# Create your views here.
def index(request):
    stores = Store.objects.all()
    context = {
        'stores': stores,
    }
    return render(request, 'index.html', context)

def detail(request, pk):
    store = Store.objects.get(pk=pk)
    context = {
        'store': store,
    }
    return render(request, 'detail.html', context)