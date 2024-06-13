import turtle as t # we can write t instead of the module name
harold = t.Turtle() # create turtle object
harold.speed(0) # this method sets the speed to very fast
colours = ["light green", "green", "blue", "purple", "blue",\
"green"]
current_colour = 0 #this keeps track of where we are in the list
for i in range(72):
    if current_colour == len(colours):
        current_colour = 0 # send us back to start of the list
harold.color(colours[current_colour])
harold.circle(100) # this method has harold draw a circle
harold.left(5)
current_colour += 1

def sum1():
    a = int(input('Enter the amount you want to add. : '))
    b = int(input('Enter the amount you want to add. : '))
    ans = a + b
    print(ans)

sum1()

def sub(num1,num2):
    ans = num1 - num2
    print(ans)


sub(20,11)
num1 = int(input('Enter the amount you want to subtract. : '))
num2 = int(input('Enter the amount you want to subtract. : '))
sub(num1,num2)

def mul(num1,num2):
    ans = num1 * num2
    return ans
print(mul(5,6))

def dev(a,b):
    ans = a / b
    return ans

input0 = int(input('Enter the input of your thing you want to devide : '))
input1 = int(input('Enter the input of your thing you want to devide : '))
print(dev(input1,input0))

def print_helpinfo():
    print("Welcome to Brick Breaker 3000")
    print("--------CONTROLS-------")
    print("\tUse arrow keys to move!")
    print("\tUse space to shoot!")

print_helpinfo()
# TYPE 1 EXAMPLES
def print_triangle(): # since its task is to print a triangle
    for i in range(5): # it does not need any input, or give output
        print("@" * i)
print_triangle()

def ask_silly_question(): # the body of the function does not have
    input("Press any key to continue: ") # to just print something
ask_silly_question()
ask_silly_question()

import random
def guess_my_number(): # bodies can be as complicated as you need
    my_number = random.randrange(1,100)
    guess = int(input("Guess a number between 1 and 10! "))
    if guess == my_number:
        print("You guessed it right!")
    else:
        print("Wrong! My number was", my_number)

guess_my_number() # we play a new game every time it's called

# TYPE 2 EXAMPLES
def double(x): # our parameter is x, which can be anything
    print(x * 2) # we do NOT write a number as our parameter
double(4) # we write the number when we CALL it, as the argument

def print_stars(number_of_stars): # use descriptive parameter names
    print("*" * number_of_stars)
print_stars(5)
# what would happen if I wrote: print_stars("ten") ?

def print_ticket_price(type, discount):
    if type == "child":
        print("Child tickets cost $3.99")
    elif type == "senior":
        print("Senior tickets cost $5.49")
    elif discount: # we expect discount to always be True or False
        print("Adult ticket with Family Discount is $6.25")
    else:
        print("Adult ticket, no discount, costs $7.25")

print_ticket_price("senior", False)
print_ticket_price("adult", True)
# what happens when you call this function with 1 argument?

# TYPE 3 EXAMPLES
def get_sum(x, y):
    return x + y
print(get_sum(10,15)) # what will this print?

def is_adult(age):
    if age > 17:
        return True
    else:
        return False
# this function has multiple return statements, but you can see that
# no matter what argument is passed in for 'age', it always returns
# just one value. There is no way the code can reach both returns!

a = is_adult(89) # what is stored in variable a?


if is_adult(10): # if is adult(10) evaluates to True, it will print
    print("10 year olds are adults") # will this be printed?

user_age = int(input("How old are you?" ))
if is_adult(user_age): # it only prints if they enter 18 or higher
    print("You are an adult.")

is_adult(99) # where is the return value going here
print_stars(28)
print_stars(52)
