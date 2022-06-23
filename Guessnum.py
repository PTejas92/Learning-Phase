import random

guess = int(input("What is your guess: "))
correct_num = random.randint(1,100)
n_count = 1

while guess != correct_num:
    n_count += 1
    if guess < correct_num:
        guess = int(input("Your guess is smaller than number"))
    else:
        guess = int(input("Your  guess is higher than number"))

print(f"You guess the correct number. you took {n_count} guesses")