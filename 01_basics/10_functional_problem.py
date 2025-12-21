#1:
# write a function to calculate and return the square of a number

# def square_num():
#    return 4 ** 2

# res = square_num()
# print(res)

#2:
#create a funtion that take parameters that return their sum

# def sum_of_two_num(a,b):
#     return a + b

# print(sum_of_two_num(4,5))

#3:
# write a funtion that multiply that multiplies two numbers, but can also accept and multiply strings

# def multiply(p1, p2):
#     return p1 * p2

# print(multiply("m", 5))

#4: 
#create a funtion that returns both the area and circumference of a circle given its radius

# import math
# def area_circumference(r):
#   area =math.ceil(math.pi * r ** 2)
#   circum =math.ceil(2 * math.pi * r)
#   return area, circum

# a, c = area_circumference(5)

# print(a, c)

#5:
# write a funtion that greets a user, if no name is provided, it shuld greet with a default name

def greet(name = "user"):
    return "hello, " + name + " !"

print(greet())


def num(a = 0, b = 0):
    return a + b

print(num(10, 20))