#ask the user to enter a word;
# use user_word = user_word.upper() to convert the word entered by the user to upper case; we'll talk about the so-called string methods and the upper() method very soon - don't worry;
# use conditional execution and the continue statement to "eat" the following vowels A, E, I, O, U from the inputted word;
# print the uneaten letters to the screen, each one of them on a separate line.

user_word = input("Please enter a word: ")
user_word = user_word.upper()

for letter in user_word:
    if letter == "A":
        continue
    if letter == "E":
        continue
    if letter == "I":
        continue 
    if letter == "O":
        continue
    if letter == "U":
        continue
    else: 
        print(letter)
