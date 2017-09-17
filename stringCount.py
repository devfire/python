#!/usr/bin/python3

testString='I wonder what the character count is in this long string.'

count={}

for char in testString:
    count.setdefault(char, 0)
    count[char] += 1

print (count)

for position in range(len(testString), 0, -1):
    print (testString[position - 1], end='')
    #print (position)
