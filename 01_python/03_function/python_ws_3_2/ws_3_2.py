name = str(input())
age = int(input())
address = str(input())

number_of_people = 0
print('현재 가입 된 유저 수 :', number_of_people)

def increase_user():
    global number_of_people
    number_of_people += 1
    return number_of_people

user_info = {}
def create_user():
    increase_user()
    user_info['name'] = name
    user_info['age'] = age
    user_info['address'] = address
    print(f'{name}님 환영합니다!')
    
    return user_info

print(create_user())

print('현재 가입 된 유저 수 :', number_of_people)