# 1. Class and the Class def and the object
class Car :
    Total_car = 0
    
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.Total_car += 1
        
    def get_brand(self):
        return self.__brand
    
    def show(self):
        return f"{self.__brand} {self.__model}"
    
    def fuel_type(self):
        return "petrol and the diesel"
    
    @staticmethod
    def general_descript():
        return "Cars is the most beautifull thing in the world that created by the human to easiar the traveling"
    
    @property
    def model(self):
        return self.__model
    

my_car = Car("mahindra", "Scorpio")
print(my_car.show())

# my_car.model = "city"
print(my_car.model)

# print(my_car.general_descript())
print(Car.general_descript())



# 2. Inheritance
class ElectricCar(Car):
    def __init__(self, brand, model, batterySize):
        super().__init__(brand,model)
        self.batterySize = batterySize
    
    def fuel_type(self):
        return "Electric charge"

        
my_tes = ElectricCar("tes", "s", "50kwh")

print(isinstance(my_tes, Car))
print(isinstance(my_tes, ElectricCar))
print()
print(my_tes.show())
print(my_tes.fuel_type())

safari = Car("tata", "safari")
print(safari.Total_car)

# 3. Encapsulation
# used the __ for the private the variable 
# can access that vriable by direct by name in object calling
# access by the getter method that return that attributes 
my_car = Car("BMW", "M1")
# print(my_car.__brand) can access it
print(my_car.get_brand())

# 4. Polymorphism
# same method that use in different class
# ex - in car and the ElectricCar we use the same method tha name is fueltype()


# 5. Class variable
# use for calculating the how many time our class has been called
# ex - in car we used the totalCar method


# 6. Static method
# this method is use for the creating the def that access only by the class not by the object

# 7. Property Decorator 
# this dont allow to change the any attributes 

# 8. isinstance() Function
# is the funtion that check whether the instance is of that class for we create

# 9. Multiple Inheritance

class Battery:
    def battery_info(self):
        return "this is battery"

class Engine:
    def engine_info(self):
        return "this is engine"

class Electriccar2(Battery, Engine, Car):
    pass

my_new1 = Electriccar2("tesla", "m")
print(my_new1.engine_info())