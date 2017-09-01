#!/usr/bin/python3

testString='I wonder what the character count is in this long string.'

count={}

for char in testString:
    count.setdefault(char, 0)
    count[char] += 1

print (count)
