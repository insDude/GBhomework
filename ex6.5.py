class Stationary:
    def __init__(self, title="Drawing something"):
        self.title = title

    def draw(self):
        print(f"Start drawing! {self.title}")

class Pen(Stationary):
    def draw(self):
        print(f"Start drawing with Pen. {self.title}")

class Pencil(Stationary):
    def draw(self):
        print(f"Start drawing with Pencil. {self.title}")

class Marker(Stationary):
    def draw(self):
        print(f"Start drawing with Marker. {self.title}")

chancellery = Pen()
chancellery.draw()
chancellery = Pencil()
chancellery.draw()
chancellery = Marker()
chancellery.draw()


