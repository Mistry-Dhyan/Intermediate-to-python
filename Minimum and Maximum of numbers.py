# max out of all
def maxnum(lst):
    big = lst[0]
    for letter in lst:
        if letter > big:
            big = letter
    return(big)

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

print('Biggest number is : ',maxnum(lst),'from',lst,'.')

# minimun out of all
def minnum(lst):
    small = lst[0]
    for letter in lst:
        if letter < small:
            small = letter
    return(small)

print('smallest number is : ',minnum(lst),'from',lst,'.')
