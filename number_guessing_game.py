# Number Guessing Game
import random
# Randomly select a number between 1 and 10
selected_number = random.randint(1, 10)

print("\nWelcome to the Number Guessing Game! I have selected a number between 1 and 10, can you guess what it is?")

user_has_guessed_correctly = False

while not user_has_guessed_correctly:
    user_input = input("\nEnter your guess here: ")
    
    if int(user_input) == selected_number:
        print("Congratulations! You've guessed the correct number!")
        user_has_guessed_correctly = True
    else:
        print("Nope, that is not the correct number.")

print("\nEnd of program") 
