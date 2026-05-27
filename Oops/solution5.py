# create a car class with attributes like brand and model .then create an instance of this class
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
class electricCar(Battery,Engine):

    def __init__(self,brand,model,battery):
        super().__init__(brand,model,"battery")
        self.battery=battery
        print("battery :",self.battery)
    
    def fuel_type(self):
        print("Fuel Type is : battery")


# print(car.total_car)
# c1.fuel_type()
# c1.show()
# c2.get_brand()
# e3=electricCar("tata","punch","20000mah")
# e3.fuel_type()
# c3.show()
# car.general_info()
