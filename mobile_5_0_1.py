import random

class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed):
        self._cords = [0, 0, 0]
        self.speed = speed

    def move(self, dx, dy, dz):
        if self._cords[2] + dz * self.speed < 0:
            print("It's too deep, i can't dive :(")
        else:
            self._cords[0] += dx * self.speed
            self._cords[1] += dy * self.speed
            self._cords[2] += dz * self.speed

    def get_cords(self):
        print(f"X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}")

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

    def speak(self):
        if self.sound is not None:
            print(self.sound)

class Bird(Animal):
    beak = True

    def lay_eggs(self):
        num_of_eggs = random.randint(1, 4)
        print(f"Here are(is) {num_of_eggs} eggs for you")

class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        self._cords[2] -= abs(dz) * (self.speed // 2)

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

# Класс Duckbill наследует Bird, AquaticAnimal и PoisonousAnimal
class Duckbill(Bird, AquaticAnimal, PoisonousAnimal):
    sound = "Click-click-click"
# Создание экземпляра утконоса
db = Duckbill(10)

# Проверка атрибутов
print(db.live)      # True
print(db.beak)      # True

# Вызовы методов
db.speak()          # Click-click-click
db.attack()         # Be careful, i'm attacking you 0_0

# Перемещение и получение координат
db.move(1, 2, 3)
db.get_cords()      # X: 10, Y: 20, Z: 30

# Погружение под воду
db.dive_in(6)
db.get_cords()      # X: 10, Y: 20, Z: 18

# Откладывание яиц
db.lay_eggs()       # Here are(is) 2 eggs for you

