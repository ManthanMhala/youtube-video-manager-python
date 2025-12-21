#1:
#Give the list of number count how many is positive

# number = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
# positive_numbers_count = 0
# for num in number:
#     if num > 0:
#         positive_numbers_count += 1
# print("Final count of positive numbers is", positive_numbers_count)

#2:
#Sum of even numbers up to given numbers n.

# n = 15
# sum_even = 0

# for i in range(1, n+1):
#     if i % 2 == 0:
#         sum_even += 1
# print(sum_even)
    
#3:
#print the multiplication table for a given number upto 10, but skip the fifth iterations.

# number = 10
# for i in range(1, 11):
#     if i == 5:
#         continue
#     print(number, "X", i, "=", number * i)

#4:
#Reverse the string using the loop

# string1 = "manthan"
# reversed_str = ""

# for char in string1:
#     reversed_str = char + reversed_str
# print(reversed_str)

#5:
# Given a string find the first non repeated char.

# string1 = "teeter"

# for char in string1:
#     print(char)
#     if string1.count(char) == 1:
#         print(char)
#         break

#6:
#compute the factorial of a number using a while loop.

# num = 6
# factorial = 1

# while num > 0:
#     factorial = factorial * num
#     num = num - 1
# print(factorial)

#7:
# keep asking the user for input util they enter a number between 1 and 10.

# while True :
#    number = int(input("Enter value form 1 to 10: "))
#    if 1 <= number <= 10:
#        print("thanks")
#        break
#    else:
#        print("invalid number try again")

#8:
# check if the number is prime of not.

# number = 18
# is_prime = True

# if number > 1:
#     for i in range(2, number):
#         if (number % i) == 0:
#             is_prime = False
#             break
# print(is_prime) 

#9:
#check if all elements in a list are unique if a duplicate is found exit the loop and print the duplicate 

# items = ["apple", "banana", "orange", "apple", "mango"]

# unique_item = set()

# for item in items:
#     if item in unique_item:
#         print("Duplicate", item)
#         break
#     unique_item.add(item)

#10:
# Implemet an exponetial backoff strategy that double the wait time between retries, starting from 1 second, but stops after 5 retries.

import time

wait_time = 1
max_tries = 5
attempts = 0

while attempts < max_tries:
    print("Attempt", attempts + 1, "wait", wait_time, )
    time.sleep(wait_time)
    wait_time *= 2
    attempts +=1