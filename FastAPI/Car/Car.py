class Car:
    def __init__(self, engine):
        self.engine = engine
        self.on = False

    def state_switch(self):
        self.on = not self.on
        print("vroom!!" if self.on else "*****")

class Engine:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

car = Car(Engine("P8", 900000))
car.state_switch()
print(car.engine.name)