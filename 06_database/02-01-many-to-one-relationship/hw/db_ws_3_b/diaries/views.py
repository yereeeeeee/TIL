from django.shortcuts import render, redirect
from .models import Diary
from .forms import DiaryForm, CommentForm

# Create your views here.
def index(request):
    diaries = Diary.objects.all()
    comments_form = CommentForm()
    context = {
        'diaries': diaries,
        'comments_form': comments_form,
    }
    return render(request, 'diaries/index.html', context)

def create(request):
    if request.method == 'POST':
        form = DiaryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('diaries:index')
    else:
        form = DiaryForm()
    context = {
        'form': form
    }
    return render(request, 'diaries/create.html', context)

def comments_create(request, pk):
    diary = Diary.objects.get(pk=pk)
    comments_form = CommentForm(request.POST)
    if comments_form.is_valid():
        comment = comments_form.save(commit=False)
        comment.diary = diary
        comment.save()
        return redirect('diaries:index')
    context = {
        'diary': diary,
        'comments_form': comments_form,
    }
    return render(request, 'diaries/index.html', context)