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

##There are many diffrences between lists and strings. One of the ways is that in strings you can't add more carectors but on a list you add stuff to it.
##Did you know that when you add more carectors to a string then you will get an error but if you add more stuff to a list then you are able to go on without a error.
