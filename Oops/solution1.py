
class car:
    total_car=0
    def __init__(self,brand,model,fuel):
        self.__brand=brand
        self.__model=model
        self.fuel=fuel
        car.total_car+=1
    def fuel_type(self):
        print("Fuel Type is :",self.fuel)

    def show(self):
        print("brand :",self.__brand)
        # print("model :",self.model)


c1=car("toyota","innova","petrol")
c2=car("suzuki","swift","diesel")