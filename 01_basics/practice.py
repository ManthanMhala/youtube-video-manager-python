import sqlite3

# x = 20
# y = x
# x = 30
# print(x)
# print(y)


# l1 = [1,2,3,4,5,6]
# l2 = l1
# l1 = [20,30,40,50,60]
# print(l1)
# print(l2)

# string = "0123456789"
# print(string[-2:])

#dictionary

# dict1 = {"creatine":"strenth", "protine":"musle recovery", "ashwgandha":"better slepp"}
# dict1["omega3"] = "recovey"
# print(dict1)
# print(dict1.popitem())
# print(dict1)

# for keys in dict1.items():
#     print(keys)
    
# if "creatines" in dict1:
#     print("i have")
# else:
#     print("i don't have")
    
# del dict1["ashwgandha"]
# print(dict1)

# tup1 = ("creatien", "protine", "ashwgandha", "omega3", "d-complex", "glutamine", "multivitamine")
# for suppl in tup1:
#     print(suppl)
# print(tup1)

# list1 = [1,2,3,4,5,6,7]
# print(list1[1]) 
# list1[0] = 34
# list1.append(12)
# print(list1)
# list1.insert(3,13)
# list1.pop()
# print(list1)

# tup1 = (1,23,4,45,6,7)
# tup1 = list(tup1)
# tup1[2] = 70
# tup1 = tuple(tup1)
# print(type(tup1))
# print(tup1)


# list1 = [12,23,34,45,56,67,78,89,90]
# reversedlist = []

con = sqlite3.connect('ty.db')
cur = con.cursor()

cur.execute('''
            CREATE TABLE IF NOT EXISTS CARS(
                name TEXT NOT NULL PRIMARY KEY,
                manufact_year TEXT NOT NULL
                )
            ''')

def add_car(car_name, manu_year):
        cur.execute('''
                INSERT INTO CARS (name,manufact_year) VALUES (?,?)''', (car_name, manu_year))
        con.commit()
    

def del_car(car_name):
    cur.execute('''
                DELETE FROM CARS WHERE NAME = ?''', (car_name,))

def shows_car():
    cur.execute(" SELECT * FROM CARS ")
    for row in cur.fetchall():
        print(row)
        
def main():
    while True:
        print("1. add the car")
        print("2. del the car")
        print("3. shows all car")
        print("4. exit")
        choice = input("Enter the choice from given below")
        
        if choice == '1':
            car_name = input("Enter the car name")
            manu_year = input("Enter the manufacturing year")
            add_car(car_name, manu_year)
        elif choice == '2':
            car_name = input("Enter the car name")
            del_car(car_name)
        elif choice == '3':
            shows_car()
        elif choice == '4':
            break
        else:
            print("Enter the correct choice")
            
    



if __name__ == "__main__":
    main()