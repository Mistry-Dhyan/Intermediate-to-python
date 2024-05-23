a = ['apple , banana , cherry , blueberry']
while True:
  for i in a:
    print(i)
  p = input('Do you want to modify or add to the list? : ')
  if p == 'add':
    d = input('what do you want to add? : ')
    a = a + [d]
#   elif p == 'modify':
#   else: start.begining()
