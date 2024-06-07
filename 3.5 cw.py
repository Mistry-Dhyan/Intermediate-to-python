secret = ['O', 'l', ' ', 'e'] # we are assembling a secret
secret.insert(1, 'n') # message!
secret.insert(3, 'y')
secret.insert(5, 'g') # write the list down on paper
secret.extend(['n', 'i', 'u']) # and track the changes
secret.append('s') # to find out what the list
secret.append('e') # becomes
secret.append('s')
for letter in " can read":
    secret.append(letter)

piece = " 012012t,,,h987i+++s823!" # when you are done,
# copy and run the code

num = len(secret) # to see if you were right!
for character in piece:
    if character.isalpha() or character == " ":
        secret.insert(num, character)
        num += 1
print(secret) # this will print a list of characters

string = "".join(secret)
print(string) # this will join the items of the list
# and make them into a string!
import math
# use this syntax to import the whole library
import random
# use this syntax if you only need one or two things
from math import floor
print(random.choice(['a', 'b', 'c'])) # usinga module function
a = 2.5
print(math.sqrt(9999999999999))+

import math
print(math.floor(2.5)) # 2.5 rounded down is 2!
print(math.ceil(2.5)) # 2.5 rounded up is 3!
print(math.fabs(2.5)) # gives us 2.5
print(math.fabs(-2.5)) # ALSO gives us 2.5
print(math.isclose(25,30,rel_tol = 10))
# 25 and 30 are less than 10 apart so this is True
print(math.isclose(3,4,rel_tol = 0.05))
# 3 and 4 are more than 0.05 apart so this is False
print(math.pow(2,3)) # 2 to the power of 3 is 8
print(math.sqrt(16)) # square root of 16 is 4
print(math.floor(math.pi)) # pi (3.14159...) rounded down is 3
print(3 > math.inf) # False! 3 is not bigger than infinity!

print(math.pi)

import random as r # now i can type r instead of the module name
col = [2,3,7,8,34,6,78,0,11,6]
print(r.choice(col))
print(r.randrange(1,10,2)) # some random odd number from 1-10
print(r.randrange(10)) # some random number from 0 - 10
print(r.sample(col, 3)) # 3 random UNIQUE items from col
print(r.choices(col, k=9)) # 9 random items from col (may repeat)

from datetime import datetime as dt
print(dt.now())
print(dt.now().weekday())
print(dt.now().date())
print(dt.now().time())

import random
import turtle
shelly = turtle.Turtle() # shelly is our turtle object
for i in range(4):
    shelly.forward(100) # use the same syntax as list or string methods
    shelly.left(90)
shelly.forward(100)

from datetime import datetime as a
days_of_the_week = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
t = a.now().weekday()
print(days_of_the_week[t])

sqrtnum = float(input('What is the number that you want to know the square of? : '))
print(sqrtnum ** 2)

lennum = len('asdfghqpwjalsie')
import random
employees = ['Sam','Bob','Max','Christopher','Alexsander','Alex','Steve','Eisenhower','Zoey','Boby','Marley','Barney','Aubin','Syed','April']
group_size= input('What is the amount of employees can you hire?(type random numbers and your employees is the lenght of it!)) : ')
while not group_size.isdigit() or int(group_size) >= lennum:
    print('Invalid input please try again.')
    group_size= input('What is the amount of employees can you hire?(type random numbers and your employees is the lenght of it!) : ')
groupe_size = int(group_size)
for i in range(len(group_size)):
    print(random.choice(employees))

import math
cridia = input('what is the diameter of  cricle? : ')
a = math.pi
print('the circumference of a cricle is', end=' ')
print(a)

import turtle
turtle.color('blue')
turtle.shape('turtle')
for i in range(5):
    turtle.forward(100)
    turtle.left(144)
