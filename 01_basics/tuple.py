cars_type = ("sedena", "4*4", "7-seaters")
print(cars_type)
# cars_type[1] =  "4*2"
print(cars_type)

more_cars = ("5-seater", "mini-van")
all_cars = more_cars + cars_type
print(all_cars)

if "4*4" in all_cars:
    print("i have")
    
more_cars = ("5-seater", "mini-van" , "5-seater")
print(more_cars.count("5-seater"))

(black, white, red) = cars_type
print(type(all_cars))