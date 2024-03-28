from django.shortcuts import render, redirect
from .models import Diary
from .forms import DiaryForm

# Create your views here.
def index(request):
  diary = Diary.objects.all()
  context = {
    'diary': diary,
  }
  return render(request, 'index.html', context)

def create(request):
  if request.method == 'POST':
    form = DiaryForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('diaries:index')
  else:
    form = DiaryForm()
  context = {
    'form': form,
  }
  return render(request, 'create.html', context)