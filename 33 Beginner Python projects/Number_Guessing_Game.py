import random

random_number = random.randint(1, 100)
print("Welcome to this number guessing game! \nIt would be truly significant if you could guess a number from 1 to 100.\nIt is not just sheer luck, it shows that the gods are by your side!")

while True:
    try:
        user_number = int(input("Guess the number from 1 to 100: "))
        if user_number == random_number:
            print("Congratulations! You guessed right!")
            break
        elif user_number < random_number - 20:
            print("Oops. You guessed too low!")
        elif user_number > random_number + 20:
            print("Oops. You guessed too high!\nGoodbye Gamer!")
            break
        else:
            print("Close but no cigar!\nGoodbye Gamer!")
            break
    except ValueError:
        print("Enter a valid number!")
        
        