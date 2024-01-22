import requests
from pprint import pprint as print

# 무작위 유저 정보 요청 경로
API_URL = 'https://jsonplaceholder.typicode.com/users'
# API 요청
response = requests.get(API_URL)
# JSON -> dict 데이터 변환
parsed_data = response.json()


dummy_data = []
for i in range(10):
    user_dict = {}
    
    user_dict['company'] = parsed_data[i]['company']['name']
    user_dict['lat'] = parsed_data[i]['address']['geo']['lat']
    user_dict['lng'] = parsed_data[i]['address']['geo']['lng']
    user_dict['name'] = parsed_data[i]['name']

    if float(user_dict['lat']) < 80 and float(user_dict['lng']) > -80 :
        dummy_data.append(user_dict)

print(dummy_data)