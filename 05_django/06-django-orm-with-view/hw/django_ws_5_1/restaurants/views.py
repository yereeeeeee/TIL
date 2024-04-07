from django.shortcuts import render, redirect
from .models import Restaurant
from .forms import RestaurantForm

# Create your views here.
def index(request):
    restaurants = Restaurant.objects.all()
    context = {
        'restaurants': restaurants,
    }
    return render(request, 'restaurants/index.html', context)

def new(request):
    form = RestaurantForm()
    context = {
        'form': form,
    }
    return render(request, 'restaurants/new.html', context)

def create(request):
    form = RestaurantForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('restaurants:index')
    context = {
        'form': form,
    }
    return render(request, 'restaurants/new.html', context)
