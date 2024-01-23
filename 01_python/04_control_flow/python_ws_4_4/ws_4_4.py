import requests
from pprint import pprint as print

# 무작위 유저 정보 요청 경로
API_URL = 'https://jsonplaceholder.typicode.com/users'
# API 요청
response = requests.get(API_URL)
# JSON -> dict 데이터 변환
parsed_data = response.json()

# 소속되어 있으면 사용자 등록 X
black_list = [
    'Hoeger LLC',
    'Keebler LLC',
    'Yost and Sons',
    'Johns Group',
    'Romaguera-Crona',
]

# 사용자 리스트(회사명, 위도, 경도, 이름)
dummy_data = []
for i in range(10):
    user_dict = {}
    
    user_dict['company'] = parsed_data[i]['company']['name']
    user_dict['lat'] = parsed_data[i]['address']['geo']['lat']
    user_dict['lng'] = parsed_data[i]['address']['geo']['lng']
    user_dict['name'] = parsed_data[i]['name']

    if -80 < float(user_dict['lat']) < 80 and - 80 < float(user_dict['lng']) < 80 :
        dummy_data.append(user_dict)

# censored_user_list라는 딕셔너리 생성 { company name : user name }
censored_user_list = {}

# 사용자 목록을 인자로 넘겨 순회하는 코드
def create_user(user_list):
    for i in range(len(user_list)):
        global censored_user_list

        # black list 확인
        if censorship(user_list[i]) == True:
        # value는 리스트로 구성
            user = []
            name = dummy_data[i]['name']
            user.append(name)
            censored_user_list[dummy_data[i]['company']] = user

    return censored_user_list



# my_dict라는 dict가 블랙리스트에 올라있는 회사 소속인과 관련된 dict인지 확인        
def censorship(my_dict):
    if my_dict['company'] in black_list:
        company = my_dict['company']
        name = my_dict['name']
        print(f'{company}소속의 {name}은/는 등록할 수 없습니다.')
        return False
    else:
        print('이상 없습니다.')
        return True
    
create_user(dummy_data)
print(censored_user_list)