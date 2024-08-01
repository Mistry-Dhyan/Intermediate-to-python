f = open('try.txt','r')
content = f.read()
print(content)
f.close()

with open('try.txt','r') as f:
    c = f.readlines()
    print(c)
f.close()

with open('add.txt','w') as f:
    f.write('hello')
f.close()

with open('try.txt','r') as f:
    c = f.readline()
    g = f.readline()
    print(c)
    print(g)
f.close()

with open('try.txt','r') as f:
    for line in f.readlines():
        print(line)
f.close()

with open('try.txt','a') as f:
    f.write('\nHello my name is Dhyan and this is me tiping with my two hands on the keyboard.')

f = open('your_name.txt','w')
name = input("What is your name, user?")
f.write("last person to run this code is: " + name + "\n")
f.close()

candy_names = []
with open('candy_text.txt' , 'r') as file:
    for line in file.readlines():
        candy_names.append(line.split(', ')[0])
    print(candy_names)


long_poem = []
with open('long_poem.txt' , 'r') as file2:
    for line in file2:
        print(line)
        file2.readline()

with open('second_poem.txt' , 'r') as file3:
    for line in file3.readlines():
        if not line == '\n' : 
            print(line)

with open('all_coders2.txt' , 'a') as file1:
    ask_ques = input('Enter your name so I can add it to my colection of coders names. : ')
    file1.write(ask_ques+"\n")

with open('file_knowledge.txt' , 'w') as file0:
    print('A file object is a way of opeing or using it. Write is the most dangerous way of using your file because it can delete all your work in the file and print what you made it write.')

