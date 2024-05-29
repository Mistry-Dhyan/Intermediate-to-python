lst = ['apple' , 'banana' , 'cherry' , 'blueberry']
while True:
    for i in lst:
        print(i,end =', ')
    print()
    p = input('Do you want to modify or add to the list? : ')
    if p == 'add':
        d = input('What do you want to add? : ')
        lst = lst + [d]
    elif p == 'modify':
        a = input('What do you want to insert? : ')
        b = input('where do you want to insert '+a+' ? : ')
        while b.isdigit() == False or  int(b) < 0 or int(b) >= len(lst):
            b = input('where do you want to insert '+a+' ? : ')
        b = int(b)
        lst[b] = a
