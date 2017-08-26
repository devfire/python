import random

print('hello world!')
print('name??')
#myName = input()
myName = "foo"

print ('good to meet you ' + myName)

print ('your name is ' + str(len(myName)))

if myName == "foo":
    print ("hello " + myName)
else:
    print ("no idea who you are!")

print ("name length is " + str(len(myName)))

nameLength = len(myName)

if nameLength > 5:
    print ("You have a long name!")
else:
    print("You have a short name!")

count = 0

while count < 5:
    count = count + 1
    print (count)

for i in range (0, 20):
    print (random.randint(0, i))
