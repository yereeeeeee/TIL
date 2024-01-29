number_of_people = 0


# def increase_user(ls, a):
#     ls.append(a)
  
def create_user(a, b, c):
    user_info = {}
    user_info['name'] = a
    user_info['age'] = b
    user_info['address'] = c
    print(f'{a}님 환영합니다!')
    
    return user_info

name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

map(create_user, name, age, address)
