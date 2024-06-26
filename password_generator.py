import random
print("\nRandom Password Generator")
print("-" * 25)

password_length = int(input("\nHow long would you like your password to be? (Recommended length is a minimum of 16 characters): "))

use_lowercase = input("Would you like to use lowercase letters in your password? (Y/N): ")
use_uppercase = input("Would you like to use uppercase letters in your password? (Y/N): ")
use_numbers = input("Would you like to use numbers in your password? (Y/N): ")
use_symbols = input("Would you like to use symbols in your password? (Y/N): ")

lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*_+?"

character_options = ""

if use_lowercase == "Y":
    character_options += lowercase

if use_uppercase == "Y":
    character_options += uppercase 

if use_numbers == "Y":
    character_options += numbers

if use_symbols == "Y":
    character_options += symbols

password = "\n"

for i in range(password_length):
    random_letter_index = random.randint(0, len(character_options) - 1)
    random_letter = character_options[random_letter_index]
    password = password + random_letter

print(password)
print("\nEnd of Program")
print()
