import math
def area_square(width):
    return width * width

def area_rectangle(width, length):
    return width * length

def area_triangle(base, height):
    return base * height / 2

def area_circle(lenght): # what information do you need?
    return lenght * lenght * math.pi # return the area of a circle
print(area_square(4)) # what is printed?
print(area_rectangle(6,10)) # what is printed?
print(area_circle(67384)) # call your circle function

name = "Robert Downey Jr."
title = "The Iron Giant"
# name and title are 'global'

def get_first_word(sentence):
    space_index = sentence.index(' ')
    first_word = sentence[:space_index]

    print(sentence)
    print(space_index)
    print(first_word) 
    # space_index, first_word, and sentence only exist here
    # they are 'local' to this function!
    # can you print name or title here? Try it out
    print(name)
    print(title)
    return first_word
# what do you think this would print? Try it out

first_of_title = get_first_word(title)
print(first_of_title)

score = 0
def check_guess(guess, answer):
    global score
    if guess.lower() == answer.lower():
        score  += 1 # an equals sign means you're reassigning score
    print(score)

guess1 = input("What is the fastest mammal in the world?")
check_guess(guess1, "Cheetah")

def employee_info(name, position = "Labourer"):
    print(name, "\t", position)

employee_info("Jenna", "Manager")
employee_info("Karim", "Supervisor")
employee_info("Paula")
employee_info("Lori")

#start
def max(*nums):
    biggest_so_far = 0 # this only works for positive numbers
    for num in nums: # nums is a collection!
        if num > biggest_so_far:
            biggest_so_far = num
    return biggest_so_far
print(max(1,2,34,7))
print(max()) # what if we give it no arguments?

def employee_info(name, position = "Labourer"):
    print(name, "\t", position)

# you can give them in any order if you use their names!
employee_info(position="Supervisor", name="Kira")

def max(*nums, positive = True):
    if not positive:
        return "This function only works for positive numbers!"
    biggest_so_far = 0 # this only works for positive numbers
    for num in nums: # nums is a collection!
        if num > biggest_so_far:
            biggest_so_far = num
    return biggest_so_far

# the collections still must come first
print(max(1,2,3,4,positive = True))
print(max(-2,-1,-10, positive = False))

# A global type of code is when the code can be acsesd from anywhere in the code.A local code is the type of code that can only be called from the code in the funtion.
# If you use the local code outside of the funtion it will give you an error or do nothing.

def minnum(lst):
    small = lst[0]
    for letter in lst:
        if letter < small:
            small = letter
    return(small)

def int_input(prompt):
    num = input(prompt)
    while num.isdigit() == False:
         num = input(prompt)
    return int(num)

lst = []
len_num = int_input('How many digits do you want to add? : ')
for i in range(len_num):
    item = int_input('Enter any digit that. : ')
    lst.append(item)

print('smallest number is : ',minnum(lst),'from',lst,'.')

names = []
usein = input("Enter a name or if you don't want to add more say done. : ")
names.append(usein)
while True:
    if 'done' in usein:
        break
    usein = input("Enter a name or if you don't want to add more say done. : ")
    names.append(usein)
for name in names:
    print(name, end='\t')


def min_version(*nums):
    small = nums[0]
    for num in nums:
        if num<small:
            small = num
    return small

print(min_version(3,6,8,-9,0,-80,99,-4))

def name_printer(*names):
    for name in names:
        print(name, end='\t')

name_printer('Bob','billy','Sam' , 'cristorpher' , 'alexzander' , 'alex')

print('\n')
def identification(name = 'N/A',phone = 'XXX-XXX-XXXX'):
    print('name : ',name,'\nphone number : ',phone)
identification('Bobey Mikflaren alexander','911-911-9111')
identification('Bobey Mikflaren alexander')
identification(phone='911-911-9111')
identification()

def area_rectangle(width):
    return width * width
print(area_rectangle(10))

def sum_or_product(*nums, bool):
    if bool == True:
        sum = 0
        for num in nums:
            sum += num
        return sum
    else:
        product = 1
        for num in nums:
            product *= num
        return product

print(sum_or_product(1,5,1,9,5,3, bool=False))

# Optional Parameters are usefull so when you are wanting to write less code and want to put a/some certain carrector/s after the words you want.
# Keyword Parameters are useful so instead, the caller (code using the function) could give information using the parameter's name!
