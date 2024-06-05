lst = []
print("Do you want to add more words to the list? If yes then what do you want to add the list. If no then write 'done' : ")
while True:
    item = input("Enter your Item : ")
    if item.lower() == 'done':
        print(lst)
        break
    lst.append(item)

while True:
    edit = input('Do you want to append(add), delete and insert or done or replace? : ')
    if edit == 'add':
        appite = input('what do you append(add) you your list? : ')
        lst.append(appite)
        print(lst)
    elif edit == 'delete':
        popnum = input('what do you want to delete? : ')
        lst.pop(popnum)
        print(lst)
    elif edit == 'insert':
        numcha = input('What do you want to change? : ')
        numadd = input('What do you want to change ' +numcha+ ' with? : ')
        while numadd.isdigit() == False:
            numadd = input('Which string number do you want to change ' +numcha+ ' with? : ')
        numadd = int(numadd)
        lst.insert(numadd,numcha)
        print(lst)
    elif edit == 'replace':
        numcha = input('What do you want to change? : ')
        numadd = input('Which string number do you want to change ' +numcha+ ' with? : ')
        while numadd.isdigit() == False:
            numadd = input('Which string number do you want to change ' +numcha+ ' with? : ')
        numadd = int(numadd)
        lst[numadd] = numcha
        print(lst)
    elif edit == 'done':
        print(lst)
        break
while True:
    editmore = input('Do you want to sort the list from a-z or reverse the whole list in your chart or both or done? : ')
    if editmore == 'sort':
        lst.sort()
        print(lst)
        break
    elif editmore == 'reverse':
        lst.reverse()
        print(lst)
        break
    elif editmore == 'both':
        lst.sort()
        lst.reverse()
        print(lst)
        break
    elif editmore == 'done':
        print(lst)
        break
