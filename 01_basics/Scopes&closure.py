name = "piyush"
def func():
    name = "chai"
    print(name)
print(name)
func()

x = 99
# def func2(y):
#     z = x + y
#     return z

# res = func2(90)
# print(res)

def func3():
    global x
    x = 12
func3()
print(x)


def f1():
    x = 88
    def f2():
        print(x)
    return f2()
myRes = f1()


def chai(num):
    def actual(x):
        return x ** num
    return actual

# def chai(2):
#     def actual(x):
#         return x ** 2
#     return actual 

f = chai(2)
g = chai(3)
print(g(2))