import random

words = ['python', 'developer', 'console', 'variable', 'list', 'syntax', 'assignment', 'comment', 'classes', 'function', 'method', 'extension', 'code', 'database', 'shell', 'feature', 'configuration', 'loop', 'while', 'elif']
selected_word = random.choice(words) #easier than indexing in other projects

guessed_spaces = ['_'] * len(selected_word)
game_over = False

print('\nWord Guessing Game') # Randomly select a word
print('-' * 18)
# display all of the unguessed letters as underscores
print('Let\'s play a word game! The word is somehow related to Python. ')

incorrect_guesses_left = 6

while not game_over:
    print(f'You have {incorrect_guesses_left} guesses remaining.')

    next_guess = input('\nPlease enter a letter: ')

    if next_guess in selected_word:
        for index, letter in enumerate(selected_word): #tells python we want a list of pairs, the index and the corresponding letter
            if letter == next_guess:
                guessed_spaces[index] = next_guess 
        joined_guesses = ''.join(guessed_spaces) 
        print(joined_guesses)       
        if joined_guesses == selected_word:
            print(f'\nCongratulations! The word is "{selected_word}." Well done!')
            game_over = True 

    else: 
        print('\nUnfortunately, that letter is not in the word.')
        incorrect_guesses_left -= 1
        if incorrect_guesses_left == 0:
            print(f'You are out of guesses. The word was "{selected_word}." Thank you for playing!')
            game_over = True
            
print('\nEnd of program')
print()
