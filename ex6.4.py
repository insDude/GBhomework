class Car:
    def __init__(self, name, color, speed, is_police):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police
        print(f"Машина: {self.name} (Цвет {self.color} Машина для полиции - {self.is_police}")

    def go(self):
        print(f"{self.name}: Машина поехала")

    def stop(self):
        print(f"{self.name}: Машина остановилась")

    def turn(self, direction):
        print(f"{self.name}: Машина повенула {'направо' if direction == 0 else 'налево'}")

    def show_speed(self):
        print(f"{self.name}: Скорость автомобиля: {self.speed}")

new_car = Car()
new_car.go()

#Не справился с добавлением дочерних классов.




