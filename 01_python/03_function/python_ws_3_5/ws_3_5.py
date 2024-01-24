name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

def create_user(a, b, c):
    user_info = {}
    user_info['name'] = a
    user_info['age'] = b
    user_info['address'] = c
    print(f'{a}님 환영합니다!')
    
    return user_info

# 모든 신규 고객 정보 딕셔너리를 요소로 갖는 리스트
many_user = list(map(create_user, name, age, address))
# print(many_user)

# 실습 3
def decrease_book(book_num):
    number_of_book -= book_num
    return number_of_book

# info 인자는 신규 고객의 이름과 나이를 담은 딕셔너리
def rental_book(info):
    info = {
        'name': '',
        'age': '',
    }

info_user = list(map(lambda x: x.items('name'), many_user))
print(info_user)