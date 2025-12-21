list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list[1:-3])

list[1:2] = [12,24]
print(list)
list.append(20)
print(list)
list.pop()
print(list)
list.insert(5, 50)
print(list)

num = [x-3 for x in range(20)]
print(num)