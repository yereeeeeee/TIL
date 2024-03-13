from django.shortcuts import render

# Create your views here.
def introduce_view(request, username):
    username = {
    'username': username
    }
    return render(request, 'introduce.html', username)
 