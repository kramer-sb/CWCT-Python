#ask the user to enter a word;
#use user_word = user_word.upper() to convert the word entered by the user to upper case;
#use conditional execution and the continue statement to "eat" the following vowels A, E, I, O, U from the inputted word;
#assign the uneaten letters to the word_without_vowels variable and print the variable to the screen.

word_without_vowels = ""

user_word = input("Enter your word: ")
user_word = user_word.upper()

for letter in user_word:
    if letter == "A":
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    else:
        word_without_vowels += letter
		
print(word_without_vowels)
