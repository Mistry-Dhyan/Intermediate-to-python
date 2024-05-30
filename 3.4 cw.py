# b = [3,5,7,8,9,0]
# a = b.sort()
# print(a)

# numbers = [3,2,1]
# numbers.sort()
# print(numbers) # the list stored in numbers is DIFFERENT now

lst = ['a', 'b', 'c', 'e', 'f']
lst.append('g') # notice we DO NOT write list =list.append('g')
print(lst)

lst.insert(3,'d')# insert item 'd' at index 3
print(lst)

lst.extend([7,8]) # extend needs a list as input!
print(lst)

lst.remove('b') # remove the ITEM 'b' from the list
print(lst)

x = lst.pop(1) # remove item at INDEX 1, and store item in x
print(x)
print(lst)

lst.sort() # now our list is sorted
print(lst)
lst.reverse() # now our list is reversed
print(lst)

# student = "Liam"
# student.upper()
# print(student)

# student = student.upper()
# print(student) # now we print "LIAM"!

# it will print None
weekdays = ['monday', 'tuesday']
weekdays = weekdays.append('wednesday')
print(weekdays)

cities = ['oakville', 'niagara falls', 'toronto', 'vaughn']
cities.append('brampton')#this will mutate
first = cities[0]
cities[0] = cities[0].upper()
print(cities[1].upper())#this will mutate

animals =['Geko','Cat','Dog','Donkey','Horse','Patato Bug']
animals.insert(2, 'Chameleon')



print(animals)
