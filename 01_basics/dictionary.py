dict1 = {"car1":"brezza", "car2":"city", "car3":"ciaz"}
print(dict1)
print(dict1["car2"])
print(dict1.get("car3"))
dict1["car2"] = "Honda city"
print(dict1)

for cars in dict1:
    print(cars, dict1[cars])
    
for cars, value in dict1.items():
    print(cars, value)

if "car2" in dict1:
    print("i have")
    
dict1["car4"] = "scorpio"
print(dict1)

dict1.pop("car2")
print(dict1)

dict1.popitem()
print(dict1)

del dict1["car1"]
print(dict1)

dict1 = dict1.copy()

cars_shop = {
    "sedan": {"maruti":"Ciaz", "honda":"city", "renualt":"kwid"},
    "7-seater":{"maruti":"ertiga", "honda":"br-v", "renualt":"triber"}
}

print(cars_shop)

print(cars_shop["sedan"]["maruti"])

squared_nun = {x:x**2 for x in range(5)}
print(squared_nun)
squared_nun.clear()
print(squared_nun)

keys = ["car1", "car2", "car3"]
print(keys)
default_value = "best"

new_dict = dict.fromkeys(keys, default_value)
print(new_dict)