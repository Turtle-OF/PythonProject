
class Anim:
    def __init__(self, ім'я, вік):
        self.ім'я = ім'я
        self.вік = вік

    def Sound(self):
        return "Ця тварина видає звук"

    def Info(self):
        return f"Ім'я: {self.ім'я}, Вік: {self.вік}"


class Dog(Anim):
    def Sound(self):
        return "Гав-гав!"


class Cat(Anim):
    def Sound(self):
        return "Мяу!"


Bars = Кіт("Барсик", 3)
Sarik = Собака("Шарик", 5)

print(барсик.інформація())
print(барсик.звук())
print(шарик.інформація())
print(шарик.звук())
