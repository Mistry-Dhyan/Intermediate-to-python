password = "U1tra_Secret_P@ssw0rd"
c = 0
s = 0
d = 0
for character in password:
    if not (character.isalnum()):
        s += 1
    elif not character.isalpha() and character.isalnum():
        d += 1
    elif character.isupper():
        c += 1
if c >= 2 and d >= 2 and s >= 2:
    print("That's a strong password!")
else:
    print("You should try to make a stronger password!")

friends = ["Noah", "Marny", "Lisa", "Gurpreet", "Isaac"]
friends = friends + ["Jenny"]
friends = friends + ["Dhyan"]
print(friends)
print(len(friends))
for name in friends:
    print(name, "is invited to my party!")
list = [1,2,3,4]
list[0] = 3
print(list)

list = ['a', 'b', 'c', 'e', 'f']
list[-0]='h'
where_is_c = list.index('c')
number_of_sevens = list.count(7)
number_of_as = list.count('a')
where_is_h = list.index('h')

class_votes = ["Jen", "Jayden", "Jared", "Jen", "Jen", "Jayden", "Jayden", "Jen"]
print(class_votes.count('Jen'))

print(class_votes.count('Jayden'))
if class_votes.count('Jen') > class_votes.count('Jayden'):print('Jen has the most votes.')
elif class_votes.count('Jen') == class_votes.count('Jayden'):print('Jayden and Jen are tied.')
else:print('Jayden has the most votes.')

friends_names = ["jeremy", "jason", "jaymit", "river","lily", "jen", "ben", "harley", "frida"]
friends_names += ['lisa','prisha','nathan']

j_counter = 0
for name in friends_names:
    if name[0] == 'j':
        j_counter+=1
        
print(j_counter)