from django.shortcuts import render
from .models import Memo

# Create your views here.
def index(request):
  memo_list = Memo.objects.all()
  context = {
    'memo_list': memo_list
  }
  return render(request, 'todos/index.html', context)