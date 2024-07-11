# def total(*nums):
#     t = 0
#     for num in nums:
#         t+=num
#     return t
# print(((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((total(1,2,3,4,5,6,7,8,9,10))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))
# more color in visoil stodio code

# def my_own_length_function (word):
#     c = 0
#     for letter in word:
#         c = c + 1
#     return c
# use_word = input('Enter a word for me to tell you the length of. : ')
# print(my_own_length_function(use_word))

# print(my_own_length_function([1,2,3,4,5,7]))

# def my_own_range_function(end,start=0,steps=1):
#     lst = []
#     c = start
#     if start<= end:
#         while c <= end:
#             lst.append(c)
#             c+=steps
#         return lst
#     else:
#         while c >= end:
#             lst.append(c)
#             c+=steps
#         return lst
# # end = input('Enter the end of your range. : ')
# # start = input("Enter the start of your range if you don't then it will got to 0. : ")
# # steps = input("Enter the steps of your range if you don't then it will got to 1. : ")
# print(my_own_range_function(10))
# print(my_own_range_function(10,start = 5))
# print(my_own_range_function(99999999, start = 1, steps = 1))
# print(my_own_range_function(1, start = 10, steps = -1))

len1 = 0
def my_own_slicing_function(word,stop_after_what):
    global len1
    for letter in range(stop_after_what):
        for letter in word:
            print(letter, end = '')
            len1 += 1
print(my_own_slicing_function('Hello my name is Dhyan',9))
