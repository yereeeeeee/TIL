# 아래 클래스를 수정하시오.
class Animal:
    pass

class Dog(Animal):
    sound = '멍멍'

class Cat(Animal):
    sound = '야옹'

class Pet(Dog, Cat):
    def __str__(self) -> str:
        return f'애완동물은 {self.sound} 소리를 냅니다.'

pet1 = Pet()
print(pet1)
