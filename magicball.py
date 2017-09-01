#!/usr/bin/python3

import random

messages = ['foo', 'bar', 'baz', 'boom']

def separate(value):
    lastIndex = len(value)
    print ('last index is ', lastIndex)
    for i in range (0, lastIndex):
        if i == lastIndex - 1:
            print (", and", value[i], end="")
        else:
            print (value[i], sep=' ', end="")


separate(messages)
print ("")
