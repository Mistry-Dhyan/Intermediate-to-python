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
