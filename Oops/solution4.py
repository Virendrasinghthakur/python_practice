
class Battery:
    def __init__(self,battery_size):
        self.battery_size=battery_size
        print(self.battery_size)

class Engine:
    def __init__(self,hp):
        self.hp=hp
        print(self.hp)

class electricCar(Battery,Engine):

    def __init__(self,brand,model,battery):
        super().__init__(brand,model,"battery")
        self.battery=battery
        print("battery :",self.battery)
    
    def fuel_type(self):
        print("Fuel Type is : battery")

