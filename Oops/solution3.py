
class Battery:
    def __init__(self,battery_size):
        self.battery_size=battery_size
        print(self.battery_size)

class Engine:
    def __init__(self,hp):
        self.hp=hp
        print(self.hp)


class electricCar(Battery,Engine):

    def __init__(self, battery_size, hp):
        Battery.__init__(self, battery_size)
        Engine.__init__(self, hp)

e=electricCar(5000,200)
print(e.battery_size )