import random

def game_intro():
    print("Men bir san saýladym. Siz ony tapyp bilersiňizmi?")
    
def choose_range():
    while True:

        minimum = int(input("Iň kiçi sany saýlaň: "))
        maximum = int(input("Iň uly sany saýlaň: "))
        if minimum < maximum:
            return minimum, maximum
        else:
            print("Iň kiçi san, iň uly sanadan az bolmaly!")
        

def generate_secret_number(minimum, maximum):
    
    return random.randint(minimum, maximum)

def get_guess():
    while True:

        guess = int(input("Sany çaklaň: "))
        return guess

def give_hint(secret_number, guess):
    if guess < secret_number:
        print("Siziň çaklamyňyz kiçi.")
    elif guess > secret_number:
        print("Siziň çaklamyňyz uly.")

def main_game():
    game_intro()
    minimum, maximum = choose_range()
    secret_number = generate_secret_number(minimum, maximum)
    attempts = 0

    while True:
        guess = get_guess()
        attempts += 1
        if guess == secret_number:
            print(f"Dogry tapdyňyz! Siz {attempts} synanşykda tapmagy başardyňyz")
            break
        else:
            give_hint(secret_number, guess)

main_game()
