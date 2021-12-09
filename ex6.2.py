class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def full_road(self):
        return f"{self._length} м * {self._width} м * 20 кг * 8 см = {(self._length * self._width * 20 * 8) / 1000} т"

new_road = Road(7000, 45)
print(new_road.full_road())
