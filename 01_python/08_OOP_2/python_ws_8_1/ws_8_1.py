# 아래 클래스를 수정하시오.
class Animal:
    # 속성 정의
    num_of_animal = 0


class Dog(Animal):
    # 생성자 수정
    def __init__(self):
        super().__init__()
        Animal.num_of_animal += 1


class Cat(Animal):
    # 생성자 수정
    def __init__(self):
        super().__init__()
        Animal.num_of_animal += 1


class Pet(Dog, Cat):
    @classmethod
    def access_num_of_animal(cls):
        return '동물의 수는 ' + str(Animal.num_of_animal) + '마리 입니다.'

dog = Dog()
print(Pet.access_num_of_animal())
cat = Cat()
print(Pet.access_num_of_animal())
