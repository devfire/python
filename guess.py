import random

print ("Welcome to the guessing game!")

computerNumber = random.randint(1,20)
enteredNumber=0
totalGuesses=0

while enteredNumber != computerNumber:
    print("Enter a number between 1 and 20: ", sep='')
    totalGuesses=totalGuesses+1
    enteredNumber=int(input())

    if enteredNumber > computerNumber:
        print ("Number is too high")
    else:
        print ("Number is too low")

print ('Congratulations, you guessed correctly in', str(totalGuesses), 'tries')
