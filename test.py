print('hello world!')
print('name??')
myName = input()

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
