# 아래 클래스를 수정하시오.
class UserInfo:
    def __init__(self):
        self.user_data = {}

    def get_user_info(self):
        try:
            print('이름을 입력하세요 : ', end='')
            name = input()
            self.name = name
            self.user_data['이름'] = self.name

            print('나이를 입력하세요 : ', end='')
            age = int(input())
            self.age = age
            self.user_data['나이'] = self.age

        except ValueError:
            print('나이는 숫자로 입력해야 합니다.')


    def display_user_info(self):
        try: 
            print('사용자 정보 : \n이름 :', self.user_data['이름'], '\n나이 :', self.user_data['나이'])
        except:
            print('사용자 정보가 입력되지 않았습니다.')


user = UserInfo()
user.get_user_info()
user.display_user_info()

