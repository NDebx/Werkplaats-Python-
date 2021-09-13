#!/usr/bin/env python
# ------------------------------------------------------------------------------------------------------------------------
# ------------ Ik moet van de boek apparte py bestanden maken maar voor gemakt doe ik het in 1 file -------------------------------
# ------------------------------------------------------------------------------------------------------------------------

# Dit is hoofdstuk 3, bijna klaar tot nu toe zou ik deze oefeningen noemen als een frisse start om alles weer even te herhalen
# 3. Executing Python – Programs, Algorithms, and Functions
# We gaan importeren dat betekent we halen functies op van een bepaald libary en deze kunnen we vervolgens bij onze code toevoegen
# Exercise 34: Writing and Executing Our First Script
import math

numbers = [5, 7, 11]
result = sum([math.factorial(n) for n in numbers])
print(result)

# vervolgens hiervan is de bedoeling dat je dan doormiddel van je shell of cmd "python example.py" doet zonder dat je op je run knop drukte
# Exercise 35: Writing and Importing Our First Module
# Ik heb hier de oude math module gebruikt en een functie aan gemaakt. 
def compute(numbers):
    return [math.factorial(n) for n in numbers]
print(compute([5,7,11]))

# Exercise 36: Adding a Docstring to my_module.py
# Ik gebruik hier de help func om bepaalde hulp te krijgen van python

#print(help(__doc__))

# Exercise 37: Finding the System Date
# Wat we hier doen is de systeem module datetime gebruiken om erachter te komen hoe laat het is
import datetime
print(datetime.datetime.now())

# Activity 8: What's the Time?
# dit opdracht is een beetje apart want het is hetzelfde als exercise 37 
import datetime
print(datetime.datetime.now())

# Exercise 38: The Maximum Number
# Deze code zoekt naar de hoogste getal binnen de lijst en vervolgens print hij die uit
l = [4, 2, 7, 3]
maximum = 0
for number in l:

    if number > maximum:

        maximum = number

print(maximum)

# Exercise 39: Using Bubble Sort in Python
# Met dit stukje code kan je een lijst sorteren op juiste volgorde 

list2 = [5, 8, 1, 3, 2]
still_swapping = True

while still_swapping:
    still_swapping = False

    for i in range(len(list2) - 1):
        
        if list2[i] > list2[i+1]:
            list2[i], list2[i+1] = list2[i+1], list2[i]
            still_swapping = True

print(list2)

# Exercise 40: Linear Search in Python
# Met dit stukje code kan je specifiek een element opzoeken in een lijst
# notitie voor mezelf deze algoritme snap ik !!!

list3 = [5, 3, 8, 4, 2]
search_for = 8
result = -1

for i in range(len(list3)):

    if search_for == list3[i]:
        result = i
        break

print(result)

# Exercise 41: Binary Search in Python
# Binary search is het zelfde als Linear Search in Python, alleen werkt het op een ander manier. Elke keer hakt hij een hele stuk eraf als hij weet dat de waarde hoger of lager is. zo hoef hij niet perse elke met elk element gaan matchen.

list4 = [2, 3, 5, 8, 11, 12, 18]
search_for_getal = 11

# hier maken we een start en end variable
slice_start = 0
slice_end = len(list4) - 1
found = False

while slice_start <= slice_end and not found:

    location = (slice_start + slice_end) // 2

    if list4[location] == search_for:
        found = True

    else:
        # Is het handig om 1 gebruiken of een ander getal. Zou dat misschien een perfomance boost geven aan mijn applicatie
        if search_for < list4[location]:
            slice_end = location - 1

        else:
            slice_start = location + 1

print(found)
print(location)

# Exercise 42: Defining and Calling the Function in Shell
# Ik moet nu een functie maken maar ik doe dat in mijn IDE en niet in me terminal omdat ik dat niet fijn vind.
# functie is iets heel belangrijk, we kunnen code schrijven die we elke keer kunnen oproepen zo hoef je niet elke keer jezelf herhalen
# Do Not Repeat Yourself (DRY)

def get_second_element(mylist):

    if len(mylist) > 1:
        return mylist[1]

    else:
        return 'List was too small'

print(get_second_element([1,2,3]))

# Exercise 43: Defining and Calling the Function in Python Script
# Dit opdracht is precies hetzelfde alleen vragen ze om het in CMD of terminal mijn script te excuten
# Deze excerises vraagt constant om een functie te maken met andere parameters en arguments

# def list_product(my_list):

#     result = 1

#     for number in my_list:
#         result = result * number

#     return result

# Ik heb een aparte file aangemaakt en de functie geimporteert 
from multiply import list_product

print(list_product([2, 3]))
print(list_product([2, 10, 15]))

# Exercise 45: Defining the Function with Keyword Arguments
# Wat hier gebeurt is we maken een functie met een pre fixed parameter en vervolgens in de tweede call geven we het een argument en dat is co.uk hiermee veranderd de pre fixed parameter 

def add_suffix(suffix='.com'):

    return 'google' + suffix

print(add_suffix())
print(add_suffix('.co.uk'))

# Exercise 46: Defining the Function with Positional and Keyword Arguments
# in de eerste call veranderen we amount naar 100 en rate blijft op zijn pre fixed waarde 
# dan berekent de code automatisch de waarde 
# in de tweede call veranderen we de pre fixed waarde van rate de functie doet altijd nog hetzelfde maar met andere data

# def convert_usd_to_aud(amount, rate=0.75):
#     return amount / rate

# print(convert_usd_to_aud(100))
# print(convert_usd_to_aud(100, rate=0.78))

# heb dit stukje eruit gecomment heb de zelfde var nodig voor andere functies

# Exercise 47: Using **kwargs
# wat hier gebeurd is. de functies roepen elkaar en uiteindelijk berekenen ze de bedragen.

def convert_usd_to_aud(amount, rate=0.75):

    return amount / rate

def convert_and_sum_list(usd_list, rate=0.75):

    total = 0

    for amount in usd_list:
        total += convert_usd_to_aud(amount, rate=rate)

    return total

print(convert_and_sum_list([1, 3]))

# Activity 9: Formatting Customer Names
# Ik heb een aparte python bestand aangemaakt voor deze activiteit heb de functie importeert en dan geroepen
# Ik snap alleen niet waarom hij none aangeeft.
# Inmiddels al opgelost, als je return gebruikt dan moet je niet gaan printen

from customer import format_customer

print(format_customer("Nilesh", "Debi", "Rotterdam"))

# Exercise 48: A Simple Function with a for Loop
# Ik snap deze opdracht niet helemaal, 100 is de parameter en uiteindelijk krijgt hij plus 1 bij elke stap van de loop maar dat zou toch 200 moeten zijn ?

# def sum_first_n(n):

#     result = 0

#     for i in range(n):
#         result += i + 1

#     return result

# print(sum_first_n(100))

# Exercise 49: Exiting the Function During the for Loop

# def is_prime(x):

#     for i in range(2, x):

#         if (x % i) == 0:

#             return False

#     return True

# print(is_prime(1000))

# Activity 10: The Fibonacci Function with an Iteration
# Ik geef eerlijk toe ik heb hierbij stackoverflow gebruikt, niet dat ik snap hoe ik dit moest bouwen maar ik snapte niet wat die fibonacci iterative is.... sorry

def fibonacci_iterative (getal): 
    a, b = 0, 1
    for i in range(0, getal):
        a, b = b, a + b
    return a

print(fibonacci_iterative(3))

# Exercise 50: Recursive Countdown
# We roepen de functie op met een getal als deze getal gelijk is aan 0 dan stop hij met tellen 

# def countdown(n):

#     if n == 0:
#         print('liftoff!')

#     else:

#         print(n)
#         return countdown(n - 1)

# print(countdown(3))

# # Exercise 51: Factorials with Iteration and Recursion
# # Wat deze code doet is, elke keer met elk verschillend element vermenigvuldigen

# def factorial_iterative(n):

#         result = 1

#         for i in range(n):
#             result *= i + 1

#         return result

# print(factorial_iterative(5))

# # De code hieronder is makkelijker te begrijpen dan hierboven
# def factorial_recursive(n):

#         if n == 1:
#             return 1

#         else:
#             return n * factorial_recursive(n - 1)    

# print(factorial_recursive(5))

# # Activity 11: The Fibonacci Function with Recursion
# # deze opdracht is hetzelfde als activity 10 
# # ik ga door naar de volgende exercise 

# # Exercise 52: Summing Integers / Exercise 53: Timing Your Code

# stored_results = {}

# def sum_to_n(n):
#     result = 0

# def sum_to_n(n):

#     result = 0

#     for i in reversed(range(n)):

#         result += i + 1

#     stored_results[n] = result
#     return result

# def sum_to_n(n):

#     result = 0

#     for i in reversed(range(n)):

#         if i + 1 in stored_results:

#             print('Stopping sum at %s because we have previously computed it' % str(i + 1))
#             result += stored_results[i + 1]
#             break

#         else:

#             result += i + 1

#     stored_results[n] = result

#     return result

# print(sum_to_n(6))

# import time

# stored_results = {}

# def sum_to_n(n):

#     start_time = time.perf_counter()

#     result = 0

#     for i in reversed(range(n)):

#         if i + 1 in stored_results:

#             print('Stopping sum at %s because we have previously computed it' % str(i + 1))

#             result += stored_results[i + 1]

#             break

#         else:

#             result += i + 1

#     stored_results[n] = result

#     print(time.perf_counter() - start_time, "seconds")

# print(sum_to_n(1000000))

# Activity 12: The Fibonacci Function with Dynamic Programming
# Deze activity bewaar ik voor de volgende keer, ik vind het fibonacci gebeuren beetje lastig

# Exercise 54: Helper Currency Conversion

# def compute_usd_total(amount_in_aud=0, amount_in_gbp=0):

#     total = 0

#     total += amount_in_aud * 0.78

#     total += amount_in_gbp * 1.29

#     return total

# print(compute_usd_total(amount_in_gbp=10))

# def convert_currency(amount, rate, margin=0):

#      return amount * rate * (1 + margin)

# def compute_usd_total(amount_in_aud=0, amount_in_gbp=0):

#     total = 0

#     total += convert_currency(amount_in_aud, 0.78)

#     total += convert_currency(amount_in_gbp, 1.29, 0.01)

#     return total   

# compute_usd_total(amount_in_gbp=10)

# Exercise 55: The First Item in a List
# Lambda is een functie om arguments en zijn functies op 1 lijn te schrijven. soort van arrow functie in Javascript

first_item = lambda my_list: my_list[0]

print(first_item(['cat', 'dog', 'mouse']))

# Exercise 56: Mapping with a Logistic Transform
# Ik moet even wennen aan de Lambda functie want je bent normaal gewent om via def etc. dan je functies op te schrijven. 

import math

nums = [-3, -5, 1, 4]

print(list(map(lambda x: 1 / (1 + math.exp(-x)), nums)))

# Exercise 57: Using the Filter Lambda
# Ja nogmaals lambda functie moet eraan wennen, heb dit niet eerder gebruik en dan ik combinatie met wiskundige berekeningen

nums = list(range(1000))

filtered = filter(lambda x: x % 3 == 0 or x % 7 == 0, nums)

print(filtered)


