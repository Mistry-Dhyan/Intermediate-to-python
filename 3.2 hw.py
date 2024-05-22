b = input('What is the amount of $ does it cost in totle? : ')
a = input('What is the amount of $ are you paying? : ')
while a == a.count('.') == 1 and a.find('.') != -1 or 0:
  a = input('What is the amount of $ are you paying? : ')
print('Your change is $', float(a) - float(b))
t = input('What is the amount of $ does it cost in totle? : ')
num = input('Enter a float number')
dot_counter = num.count('.')
dot_place = num.find('.')
whole_part = num[:dot_place]
decimale_part = num[dot_place + 1:]

while dot_counter != 1 or dot_place == -1 or dot_place == 0 or whole_part.isdigit(
) == False or decimale_part.isdigit() == False:
  print('Invalid Input')
  num = input('Enter a float number')
  dot_counter = num.count('.')
  dot_place = num.find('.')
  whole_part = num[:dot_place]
  decimale_part = num[dot_place + 1:]

print('Your change is $', float(num) - float(t))
num = float(num)
print(num, type(num))

a = input('enter a string for me to tell the length of : ')
b = len(a)
print(len(a))



a = input('enter your your user name for me to make it stronger! : ')
peidot_counter = a.count('.')
dot = a.find('.')
at_counter = a.count('@')
while peidot_counter != 1 and dot != -3 and at_counter != 1:
  print('not strong enough! : ')
  a = input('enter your your user name for me to make it stronger! : ')
  at_counter = 0
  peidot_counter = 0
  peidot_counter = a.count('.')
  dot = a.find('.')
  at_counter = a.count('@')
print(a,'strong enough!')
print('In fact that',a,'is almost the best username in the world!')
