import random

random_num = random.randint(1, 100)

chance = 5

print("Guess the number 1 and 100. You have 5 chances.")

for i in range(1, chance + 1):
    guess = int(input(f"Chance {i}: Enter your guess: "))

    if guess == random_num:
        print("Congratulation! You guessed the correct number.")
        break
    
    elif guess < random_num:
        print("Too low!")
    else:
        print("Too high!")
    
    if i == chance - 1:
        print(f"Sorry, you've used all your chances. The correct number was {random_num}")
