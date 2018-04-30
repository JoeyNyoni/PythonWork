import random

print ("Hello. How much money do you have?")
amount = raw_input()

print("Oh I see you have R" + amount)
minAmount = 1
maxAmount = 50
myAmount = random.randint(minAmount, maxAmount)

dialog = "The money I have is between R{0} and R{1}"
print(dialog.format(minAmount, maxAmount))

isFound = False
while not isFound:
    print("Guess how much I have")
    guess = int(input())
    if guess > myAmount:
        print("Too much. Go Lower!")
    if guess < myAmount:
        print("Too low. Go Higher!")
    if guess == myAmount:
        isFound = True

print ("That's right!")