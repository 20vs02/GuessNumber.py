# interactive number guessing game
# generate random number

import random
# random number between 1 and 100
randomNumber = random.randint(1, 100)
print('''In this game you must guess a random number between 1 and 100 correctly, while having a specific number of tries, in order to win.
At first you enter a mode and simultaneously you get an amount of tries. To enter a mode, please consider:
Mode:        Number of tries:
Normal       12
Challenge    8
Monster      6 
A try is a question, in which the entered number is greater or less or equal to the random number
You win, if you found the number before your tries run out
You lose, if you did not find the number before your tries run out''')

# generate mode
mode = str(input("Mode: "))
if mode == "Normal":
    tries = 12
elif mode == "Challenge":
    tries = 8
elif mode == "Monster":
    tries = 6
else:
    print("Enter a mode from above to begin")
    exit()

# for loop from 1 to number of tries

for i in range(1, tries + 1):
    guess = int(input("Enter your guessing number here: "))

    if guess == randomNumber:
        print()
        print("You win. You found this number.")
        print("mode: " + str(mode) + ", number of tries: " + str(tries))
        print(str(i) + " / " + str(tries))
        exit()
    elif guess < randomNumber:
        print()
        print("Searched number is greater than your guess")
        print(str(i) + " / " + str(tries))
        print()
    elif guess > randomNumber:
        print()
        print("Searched number is less than your guess")
        print(str(i) + " / " + str(tries))
        print()

print()
print("You lost. You couldn´t find that number")
print("That number is " + str(randomNumber))
print("mode: " + str(mode) + ", number of tries: " + str(tries))
print()
print()
exit_key = input('Press any key to exit: ')
