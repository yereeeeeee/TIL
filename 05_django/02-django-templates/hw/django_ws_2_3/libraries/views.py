from django.shortcuts import render
import requests

API_URL = 'http://www.aladin.co.kr/ttb/api/ItemList.aspx'
API_KEY = '###'
# Create your views here.
def index(request):
    return render(request, 'index.html')

def recommend(request):
    params = {
        'ttbkey': API_KEY,
        'QueryType': 'ItemNewSpecial',
        'MaxResults': '50',
        'start': '1',
        'SearchTarget': 'Book',
        'output': 'js',
        'Version': '20131101'
    }

    response = requests.get(API_URL, params=params).json()
    result = []
    for item in response['item']:
        info = {
            'title': item['title'],
            'author': item['author'],
            'pubDate': item['pubDate'],
            'isbn': item['isbn'],
        }
        result.append(info)
    print(result)
    context = {
        'result': result
    }
    return render(request, 'index.html', context)