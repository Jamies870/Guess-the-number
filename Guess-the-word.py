name = input ("What is your name?")
print ("Hello " + name)
choice = input ("Do you wnat to play a game?")

while True:
    user_input = input("Type 'play' to continue")

    if user_input == "play":
        break 
    else:
        print("Are you sure?")

print ("Then let's start")

secret = 90

guess = int(input("Guess the number: "))
if guess == secret:
    print("Good Job!")
else:
    name = input ("Try again?")

print ("goodluck")

secret = 67
guess = int(input("Guess the number: "))
if guess == secret:
    print("Good Job!")
else:
    name = input ("Try again one last time?")

    print ("Alright, Last Chance..")

secret = 45
guess = int(input("Guess the number: "))
if guess == secret:
    print("Finally, Good Job!")
else:
    print ("You did your best.")
    print ("Goodbye.")

