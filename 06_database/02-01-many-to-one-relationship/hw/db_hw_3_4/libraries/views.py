from django.shortcuts import render, redirect
from .models import Author
from .forms import BookForm

# Create your views here.
def index(request):
    authors = Author.objects.all()
    context = {
        'authors': authors
    }
    return render(request, 'libraries/index.html', context)

def detail(request, author_pk):
    author = Author.objects.get(pk=author_pk)
    addbook_form = BookForm()
    books = author.book_set.all()
    context = {
        'author': author,
        'addbook_form': addbook_form,
        'books': books,
    }
    return render(request, 'libraries/detail.html', context)

def create(request, pk):
    author = Author.objects.get(pk=pk)
    addbook_form = BookForm(request.POST)
    if addbook_form.is_valid():
        book = addbook_form.save(commit=False)
        book.author = author
        book.save()
        return redirect('libraries:detail', author.pk)
    context = {
        'author':author,
        'addbook_form': addbook_form,
    }
    return render(request, 'libraries/detail.html', context)