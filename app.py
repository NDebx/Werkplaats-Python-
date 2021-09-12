#Exercise 1: Getting to Know the Order of Operations
#Subtract 5 to the 3rd power, which is 53, from 100 and divide the result by 5.
print((100 - 5 ** 3) / 5)

#Add 6 to the remainder of 15 divided 4. 
print(6 + 15 % 4)

#Add 2 to the 2nd power, which is 22, to the integer division of 24 and 4. 
print(2 ** 2 + 24 // 4)

#Exercise 2: Integer and Float Types
#Begin by explicitly determining the type of 6 using the following code.
print(type(6))

#Now, enter type(6.0) in the next cell of your notebook.
print(type(6.0))

#Now, add 5 to 3.14. Infer the type of their sum. 
print(5 + 3.14)

#Now, convert 7.999999999 to an int. 
print(int(7.99999999999999))

#Convert 6 to a float.
print(float(6))

#Exercise 3: Assigning Variables
#Set x as equal to the number 2.
x = 2
print(x)

#Change x to 3.0 and add 1 to x
x = 3.0
x += 1 
print(x)

#Activity 1: Assigning Values to Variables
#First, set 14 to the x variable.
#Now, add 1 to x.
#Finally, divide x by 5 and square it.
#You should get the following output
# ik doe even x vervangen door y omdat hij eerder gedecladeerd is. 

y = 14 
y += 1 
print((y / 5) ** 2)

#Activity 2: Finding a Solution Using Pythagorean Theorem in Python.

x, y, z = 2, 3, 4
w_squared = x**2 + y**2 + z**2
w = w_squared ** 0.5
print(w)

#Exercise 4: Variable Names
#Create a variable called 1st_number and assign it a value of 1. opdracht wilt dat ik een var maakt die begint met een getal maar dat mag niet als je een var maakt. 

first_number = 1
#opdracht wilt dat ik een special char gebruikt in een var maar dat kan niet. 

my_money = 1000.00

#Exercise 5: Multiple Variables in Python
#Assign 5 to x and 2 to y:

x = 5 
y = 2

#Add x to x and subtract y to the second power:

print(x + x - y ** 2)

#Assign 8 to x and 5 to y in one line:

x, y = 8, 5

print(x // y)

#Exercise 6: Comments in Python

#Dit is een commentaar

#set the var pi eq to 3.14
pi = 3.14 
pi = 3.14       #set the var pi eq to 3.14

#Activity 2 solution with the help of pythagoras
# var aanmaken voor x,y,z die op logische volgorde waarde 2,3,4 krijgen
x,y,z = 2,3,4
#ik maak het kwadraat var om de berekening makkelijk uit te kunnen afronden
w_squared = x**2 + y**2 + z**2
print(w_squared)
#var voor w_sqaured aanmaken en deze uitprinten
w = w_squared ** 0.5
print(w)

#Activity 3: Using the input() Function to Rate Your Day
#Dag beoordeling 
day_rating = input("Day:")
print("You feel like a" +" "+day_rating + " " + "Today. Thanks for letting me know")

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 
#Ik besefte vanaf dit punt dat ik machine learning opdrachten zat te maken.. vandaar dat sommige opdrachten hier boven niet klopen !!!!!!!!!!!!!!!!!!!!!!!!!!!!
#Ik ga nu verder met opdracht zeven 
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#Exercise 7: String Error Syntax
#The goal of this exercise is to learn appropriate string syntax:

#Enter valid string
bookstore = 'City Lights'

#Enter invalid string
#boekenwinkel = 'City light" heb dit stukje eruit gecomment anders werkt me app niet meer

#Bookstore opnieuw formateren
bookstore = "Moe\'s"

#Bookstore opnieuw formateren met verkeerde qoutes 
#Bookstore = 'Moe's' ik heb dit even eruit gecomment anders werkt me app niet maar ik snap wel dat je moet opletten hoe je je strings op moet schrijven... 

#Exercise 8: Displaying Strings
#opdracht vraagt om een var te kunnen laten printen met de printfunc 

Greeting = 'Hello'
print(Greeting)
spanish_greeting = 'Hola,'
print(spanish_greeting)
arabic_greeting = 'Ahlan wa sahlan.'
print(arabic_greeting)

#Exercise 9: String Concatenation
print(spanish_greeting + " " + "senior.")

# hier print ik greeting 5 keer achterelkaar 
print(Greeting * 5)

#formatteren
owner = 'Lawrence Ferlinghetti'
test = "nilesh"
age = 100

#tip voor mezelf, format is soort van temp literal in JS
print('The founder of City Lights Bookstore, {}, is now {} years old.'.format(owner, age))

#Exercise 10: String Methods
name = "Nilesh"
print(name.lower())
print(name.capitalize())
print(name.upper())

#Exercise 11: Types and Casting
#Ik heb hier de strings nog niet geformat naar int dus hij plakt letterlijk tegen elkaar omdat het strings zijn maar inde volgend stukje niet.
vijfstr = "5"
print(type(vijfstr))
zevenstr = "7"
print(type(zevenstr))
print(vijfstr+zevenstr)

#String convert naar int 
#print(type(int(vijfstr)))
#print(type(int(zevenstr)))

print(int(zevenstr) + int(vijfstr))

#Exercise 12: The input() Function and Activity 3
name = input("What is your name?: ")
print("Hello, " + str(name) + ".")

#Activity 3 hier print ik mijn naam en wat ik van het weer vind
cijfer_weer = input("wat vind je van het weer welk cijfer geef je het?: ")
print("Hallo" + str(name) + "dus jij geef de weer vandaag een" + cijfer_weer)


#Exercise 13: Boolean Variables
#In deze oefening gaan we werken met bools. dat zijn waarden die true en false betekenen. dit kan je bijvoorbeeld toepassen bij een keuze programma of als een controle.

over_18 = True
over_21 = False
#Nu print ik zijn waardes.
print(type(over_18))
print(type(over_21))

#Exercise 14: Comparison Operators
#Nu gebruiken we operators om var's met elkaar te vergelijken

age = 20
print(age < 13)
#Hierboven zegt hij false omdat 13 kleiner dan 20 is.
#Ik check de var's en vergelijk ze ook zie in console voor uitslagen dit hoort bij de opdracht
print(age >= 20 , age <= 21 , age != 21 , age == 19 , 6 == 6.60 , 6 == '6')
print((age >= 20 and age < 30) or (age >= 30 and age < 40))

#Exercise 15: Comparing Strings
#Nu gaan we strings met elkaar vergelijken 

print('a' < 'c')
print("New York" > "San Francisco")

#Exercise 16: Using the if Syntax
#Nu werken we met if statement, dit is het zelfde als bijvoorbeeld: "Stel dit gebeurd er" dan volgt er meestal een else statement en dat is dan weer "Anders gebeurd dit"
#We gebruiken de oude age var

if age >= 18:
    print("you can vote")
    if age >= 21:
        print("You can play poker.")

#Exercise 17: Using the if-else Syntax
#We gebruiken nu de else statement de uitleg gaf ik al eerder aan, deze statement is bijna altijd in combinatie met de else statement
#Als je nu heel logisch dit bekijk dan is hiervoor geen verdere uitleg nodig 

if age < 18:
  print('You aren\'t old enough to vote.')
else:
    print('Welcome to our voting program.')

#Exercise Elif
#Elif is hetzelfde als if alleen stel je hebt meerdere scenerio's om te controleren dan is het handig om dit te gebruiken.

if age <= 10:
  print('Listen, learn, and have fun.')
elif age<= 19:
  print('Go fearlessly forward.')
elif age <= 29:
  print('Seize the day.')
elif age <= 39:
  print('Go for what you want.')
elif age <= 59:
  print('Stay physically fit and healthy.')
else:
  print('Each day is magical.')

#Exercise 18: Calculating Perfect Squares

# Number = input("Enter a nummer to see if it\'s a perfect square: ")
# Number = abs(int(Number))
# i = -1
# square = False

# while i <= Number**(0.5):
#     i += 1
#     if i*i == Number:
#         square=True
#         break
#     if square:
#         print("The sqaure root of number is i")
#     else:
#         print("number is not a perfect sqaure")


#Exercise 19: Real Estate Offer
# print('A one bedroom in the Bay Area is listed at $599,000')
# offer = abs(int(input()))
# print('Enter your best offer on the house.')
# best = abs(int(input()))
# print('How much more do you want to offer each time?')
# increment = abs(int(input()))
# offer_accepted = False
# while offer <= best:
#     if offer >= 650000:
#         offer_accepted = True

#         print('Your offer of', offer, 'has been accepted!')
#         print('We\'re sorry, you\'re offer of', offer, 'has not been accepted.' )
#         offer += increment
#         break

#Exercise 20: Using for Loops
#for loops gebruiken we om lijsten door te lopen zonder handmatig dat te checken 
for each_letter in 'Portland':
    print(each_letter)

for each_cijfer in range(1,10):
    print(each_cijfer)

for each_cijfer in range(10):
    print(each_cijfer)

for each_cijfer in range(1, 11, 2):
    print(each_cijfer)

for each_cijfer in range(3, 0, -1):
  print(each_cijfer)

name = 'Corey'
for each_letter in range(3):
  for each_cijfer in name:
    print(each_cijfer)

#laatste activiteit robot maken die praat met je. 
#deze bot houd van eten dus hij praat veel over eten :}
print("Haiii, ik ben een chef.")

lekker_eten = input("wat is je fav eten: ")
if lekker_eten == lekker_eten:
    print("oh dat is lekker")

fav_food_to_cook_with = input("Wat zijn je favorieten ingredienten om mee te koken: ")
if fav_food_to_cook_with == fav_food_to_cook_with:
    print("dat zijn hele lekkere ingredienten om mee te koken," + " " + "Ik lust ook" + " " + fav_food_to_cook_with)
    print("Ik zal iets lekkers voor je klaar maken met de ingreddienten die je hebt, maar dan wil ik graag van jou RAM als toetje :)")
    




































