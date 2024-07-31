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
