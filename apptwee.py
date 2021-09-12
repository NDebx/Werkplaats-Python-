# Hoofdstuk 2, H1 heb ik al gemaakt en zit in een aparte py-file
# Exercise 21: Working with Python Lists
# We gaan nu lijsten maken, lijsten zijn eigenlijk var's met meerdere data erin
# shopping = ["bread","milk", "eggs"]
# print(shopping)
# Hier print de for loop func alle items in shopping
# for each in shopping:
#     print(each)
# Nu maken weer een lijst maar met verschillende data types
from typing import final


mixed = [365, "days", True]
print(mixed)

# Exercise 22: Using a Nested List to Store Data from a Matrix
# Nu gaan we een list in een list maken
m = [[1, 2, 3], [4, 5, 6]]
print(m[1][1])

for i in range(len(m)):
    for j in range(len(m[i])):
        print(m[i][j])

for row in m:
    for col in row:
        print(col)

for row in m:
    for elem in row:
        print(elem)

# Activity 6: Using a Nested List to Store Employee Data
Employee = [
    ["John Mckee", 38, "Sales"],
    ["Lisa Crawford", 29, "Marketing"],
    ["Sujan Patel", 33, "HR"],
]
print(Employee[1])

# Exercise 23: Implementing Matrix Operations (Addition and Subtraction)
# X = [[1,2,3],[4,5,6],[7,8,9]]
# Y = [[10,11,12],[13,14,15],[16,17,18]]

# result = [[0,0,0],
#     [0,0,0],
#     [0,0,0]]

# for i in range(len(X)):
#     for j in range(len(X[0])):
#         result[i][j] = X[i][j] + Y[i][j]

# print(result)

# X = [[10,11,12],[13,14,15],[16,17,18]]
# Y = [[1,2,3],[4,5,6],[7,8,9]]

# result = [[0,0,0],
#     [0,0,0],
#     [0,0,0]]

# for i in range(len(X)):
#       for j in range(len(X[0])):
#         result[i][j] = X[i][j] - Y[i][j]


# print(result)

# Exercise 24: Implementing Matrix Operations (Multiplication)

X = [[1, 2], [4, 5], [3, 6]]
Y = [[1, 2, 3, 4], [5, 6, 7, 8]]

result = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

for i in range(len(X)):
    for j in range(len(Y[0])):
        for k in range(len(Y)):
            result[i][j] += X[i][k] * Y[k][j]

for r in result:
    print(r)

# Exercise 25: Basic List Operations
# Met len kunnen we de aantal elementen bepalen hoeveel er in een lijst zich bevinden
# shopping = ["bread", "milk", "eggs"]
# print(len(shopping))

list1 = [1, 2, 3]
list2 = [4, 5, 6]

final_list = list1 + list2
print(final_list)

list3 = ["oi"]
print(list3 * 3)

# Exercise 26: Accessing an Item from Shopping List Data
# Nu kunnen we element specifiek selecteren van een list
# shopping = ["bread", "milk", "eggs"]
# print(shopping[1])
# shopping[1] = "banana"
# print(shopping[1])
# print(shopping[-1])
# # Nu gaan we list door midden snijden oftewel slicen
# print(shopping[0:2])
# print(shopping[0:3])
# print(shopping[1:])

# Exercise 27: Adding Items to Our Shopping List
# We gaan nu items toevoegen aan onze shopping list dmv de append() func
# shopping = ["bread", "milk", "eggs"]
# shopping.append("apple")
# print(shopping)
shopping = []
shopping.append("bread")
shopping.append("milk")
shopping.append("eggs")
shopping.append("apple")
print(shopping)

shopping.insert(2, "ham")
print(shopping)

# Dictionary Keys and Values
# Exercise 28: Using a Dictionary to Store a Movie Record

movie = {
    "title": "The Godfather",
    "director": "Francis Ford Coppola",
    "year": 1972,
    "rating": 9.2,
}
print(movie["year"])

# Hier updaten ik de movie rating
movie["rating"] = (movie["rating"] + 9.3) / 2
print(movie["rating"])

movie["actors"] = ["Marlon Brando", "Al Pacino", "James Caan"]
movie["other_details"] = {"runtime": 175, "language": "English"}

print(movie)

# Activity 7: Storing Company Employee Table Data Using a List and a Dictionary
# Het stukje code functioneert wel alleen niet exact als de boek hoe het eist
employees = [
    {"Name": ["John McKee", "Lisa Crawford", "Sujan Patel"]},
    {"Age": [38, 29, 33]},
    {"Department": ["Sales", "Marketing", "HR"]},
]
print(employees[0]["Name"][2], employees[1]["Age"][2], employees[2]["Department"][2])

# Exercise 29: Using the zip() Method to Manipulate Dictionaries
# Door zip kunnen we de data manipuleren waardoor we ze bij elkaar kunnen toevoegen.
# items = ["apple", "orange", "banana"]
# quantity = [5, 3, 2]
# orders = zip(items, quantity)
# print(orders)
# print(list(orders))
# orders = zip(items, quantity)
# print(dict(orders))

# Exercise 30: Accessing a Dictionary Using Dictionary Methods
# Door deze techniek krijgen ik toegang tot de dictionary
orders = {"apple": 5, "orange": 3, "banana": 2}
print(orders.values())
print(list(orders.values()))
print(list(orders.keys()))

# Door deze for loop kunnen we langs elk item met zijn key langs
for tuple in list(orders.items()):
    print(tuple)

# Exercise 31: Exploring Tuple Properties in Our Shopping List
# Met tuple kunnen een lijst maken die NIET AANPASBAAR IS !!!!
t = ("bread", "milk", "eggs")
print(len(t))
# t.append("apple")
# t[2] = "apple"
print(t + ("apple", "orange"))
print(t)

t_mixed = "apple", True, 3
print(t_mixed)
t_shopping = ("apple", 3), ("orange", 2), ("banana", 5)
print(t_shopping)

# Exercise 32: Using Sets in Python
# Hij filtert de lijsten
s1 = set([1, 2, 3, 4, 5, 6])
print(s1)
s2 = set([1, 2, 2, 3, 4, 4, 5, 6, 6])
print(s2)
s3 = set([3, 4, 5, 6, 6, 6, 1, 1, 2])
print(s3)

# Als je deze curly brackets gebruikt dan gaat hij random de data representeren
s4 = {"apple", "orange", "banana"}
print(s4)

# Sets kan je constant aanpassen
# alleen gebruiken hierbij add func en geen append want append doen we voor andere lists
s4.add("pineapple")
print(s4)

# Exercise 33: Implementing Set Operations
# Hierbij gebruiken we 2 technieken om set's met elkaar te kunnen verbinden
s5 = {1, 2, 3, 4}
s6 = {3, 4, 5, 6}
print(s5 | s6)
print(s5.union(s6))
# met difference kan je verschillen zoeken tussen set's
print(s5 - s6)
print(s5.difference(s6))
# met issubset controleer je de sets met elkaar of ze bijelkaar horen
print(s5 <= s6)
print(s5.issubset(s6))
s7 = {1, 2, 3}
s8 = {1, 2, 3, 4, 5}
print(s7 <= s8)
print(s7.issubset(s8))
# standaard logica operators
print(s7 < s8)
s9 = {1, 2, 3}
s10 = {1, 2, 3}
print(s9 < s10)
print(s9 < s9)
# operator die controleert of ze bijelkaar horen
print(s8 >= s7)
print(s8.issuperset(s7))
print(s8 > s7)
print(s8 > s8)
