def total(*nums):
    t = 0
    for num in nums:
        t+=num
    return t
print(((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((total(1,2,3,4,5,6,7,8,9,10))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))
# more colors in VSC or you can call it Visual Studio Code.

def my_own_length_function (word):
    c = 0
    for letter in word:
        c = c + 1
    return c
use_word = input('Enter a word for me to tell you the length of. : ')
print(my_own_length_function(use_word))

print(my_own_length_function([1,2,3,4,5,7]))

def my_own_range_function(end,start=0,steps=1):
    lst = []
    c = start
    if start<= end:
        while c <= end:
            lst.append(c)
            c+=steps
        return lst
    else:
        while c >= end:
            lst.append(c)
            c+=steps
        return lst
# end = input('Enter the end of your range. : ')
# start = input("Enter the start of your range if you don't then it will got to 0. : ")
# steps = input("Enter the steps of your range if you don't then it will got to 1. : ")
print(my_own_range_function(10))
print(my_own_range_function(10,start = 5))
print(my_own_range_function(99999999, start = 1, steps = 1))
print(my_own_range_function(1, start = 10, steps = -1))

len1 = 0
def my_own_slicing_function(lst,start = 0, end = -1, steps = 1):
    nlst = []
    if end == -1:
        end = len(lst)
    
    for i in range(start,end,steps):
        nlst.append(lst[i])
    return nlst
    
print(my_own_slicing_function([1,2,3,4,5,6,7,8,9,0],1,steps=2))
print(my_own_slicing_function([1,2,3,4,5,6,7,8,9,0],8,1,steps=-3))
print(my_own_slicing_function('aswHveslglsog amfya fnaafmaed aifsd aDdhaydaana!adaw',3,49,2))

This_is_a_Global_variable = ('this is a global variable')
print(This_is_a_Global_variable)
# All the local variables in this whole code are nums , t , c , leter , word , lst , start , end , nlst , steps , string , & i are all of them!
# All the global variables in this whole code are none , there are no global variables in my code!
def my_own_slicing_function_for_strings(string,start = 0, end = -1, steps = 1):
    nlst = ''
    if end == -1:
        end = len(string)
    for i in range(start,end,steps):
        nlst += string[i]
    return nlst

print(my_own_slicing_function_for_strings('aswHveslglsog amfya fnaafmaed aifsd aDdhaydaana!adaw',3,49,2))
