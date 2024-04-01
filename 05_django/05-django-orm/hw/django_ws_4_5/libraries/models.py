from django.db import models
import requests

# Create your models here.
class Book(models.Model):
    isbn = models.CharField(max_length=10)
    author = models.TextField()
    title = models.TextField()
    categoryName = models.TextField()
    categoryId = models.IntegerField()
    priceSales = models.IntegerField()
    priceStandard = models.IntegerField()
    pubDate = models.DateField()

    @classmethod
    def insert_data(cls):
        API_KEY = '#'
        params = {
            'ttbkey': API_KEY,
            'QueryType': 'ItemNewAll',
            'MaxResults': 10,
            'start': 1,
            'SearchTarget': 'Book',
            'output': 'js',
            'Version': '20131101',
        }
        response = requests.get('http://www.aladin.co.kr/ttb/api/ItemList.aspx', params=params)
        data = response.json()
        # print(data)

        for item in data['item']:
            params = {
                'isbn': item['isbn'], 
                'author': item['author'],
                'title': item['title'],
                'categoryName': item['categoryName'],
                'categoryId': item['categoryId'],
                'priceSales': item['priceSales'],
                'priceStandard': item['priceStandard'],
                'pubDate': item['pubDate'],
            }
            book = cls(**params)
            book.save()