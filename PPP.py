
class car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def __str__(self):
        return f"{self.color} {self.brand}"


class Garage:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cars = []

    def park_car(self, car):
        if len(self.cars) < self.capacity:
            self.cars.append(car)
            print(f"{car} заехал у гараж")
        else:
            print("Гараж повный", car)

    def show_garage(self):
        if not self.cars:
            print("Гараж пустой")
        else:
            print("в гареже:")
            for car in self.cars:
                print("-", car)

# Симуляція
car1 = Car("Tesla", "Синия")
car2 = Car("BMW", "Чёрная")
car3 = Car("Lada", "Зеленая")

garage = Garage(capacity=2)
garage.park_car(car1)
garage.park_car(car2)
garage.park_car(car3)

garage.show_garage()
