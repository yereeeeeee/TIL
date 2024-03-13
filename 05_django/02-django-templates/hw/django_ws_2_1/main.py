import requests

API_URL = 'http://www.aladin.co.kr/ttb/api/ItemList.aspx'
API_KEY = '###'

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
        '제목': item['title'],
        '저자': item['author'],
        '출간일': item['pubDate'],
        '국제 표준 도서 번호': item['isbn'],
    }
    result.append(info)
print(result)