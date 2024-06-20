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
