# # Timing function 
import time

# def timer_cal(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result =  func(*args, **kwargs)
#         end = time.time()
#         print(f"{func.__name__} ran in {end-start} time")
#         return result
#     return wrapper

# @timer_cal
# def example_func(n):
#     time.sleep(n)
    
# example_func(2)

# create the decorators to print the function and the values of its args every time the funtion is called
 
# def debug(func):
#     def wrapper(*args, **kwargs):
#         args_val = ', '.join(str(arg) for arg in args)
#         return func(*args, **kwargs)
        
#     return wrapper
 

# def greet(name, greeting="Hello"):
#     print(f"{greeting}, {name}")
    
# greet("piyush", greeting="hanji")

# Own
def check(n1):
    def wrapper(n):
        if type(n) == str:
            print("yes")
        else:
            print("no") 
        
        resu = n1(n)
        return resu
    return wrapper
@check
def print2(n):
    print(f"{n} Welcome to yourself")
    
print2("piyush")


def cache(func):
    cache_value = {}
    print(cache_value)
    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]
        result = func(*args)
        cache_value[args] = result
        return result
    return wrapper

@cache
def long_running(a,b):
    time.sleep(4)
    return a + b
print(long_running(2,3))
print(long_running(2,3))
print(long_running(4,5))
