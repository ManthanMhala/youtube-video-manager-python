print('hello', "hello1", """hello2""")
string = "0123456789"
# practice the slicing
print(string[1:])


#string method
string2 = "    manthanmantmant    "
print(string2.upper())
print(string2.lower())
print(string2.strip())
print(string.replace("1234", "887799"))
print(string2.find("mant"))
print(string2.count("man"))

# format to add the variable in the string
cars1 = "scorpio"
quantity = 10
price = "18,00,000"

orders = "the ordered car is {} and the quantity is {} also price of this car is the {}"
print(orders.format(cars1, quantity, price))

#for raw string
cars = r"scorpio,scorpio\n two types"
print(cars)

print("1234" in string)