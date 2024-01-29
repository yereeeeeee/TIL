# 아래 클래스를 수정하시오.
class Animal:
    pass

class Cat(Animal):
    def __init__(self, sound) -> None:
        super().__init__()
        self.sound = sound

    def meow(self):
        print(f'{self.sound} !')


cat1 = Cat("야옹")
cat1.meow()
