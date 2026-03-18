"""
Guess the Word

Description:
Create a word-guessing game where the player tries to discover a secret
word by entering one letter at a time. The program should reveal the
correctly guessed letters in their positions and mask the remaining
letters with "*". The game continues until the player guesses the full
word or chooses to exit.

Concepts used:

- while loops
- functions
- lists
- string iteration
- conditional statements
- user input handling

"""

from random import choice

'''  GLOBAL VARIABLES  '''

secret_words_list = ["mushroom", "lizard", "hole", "sorcerer", "bug", "smoke", "magic", "devil", "mutation", "dorohedoro"]
secret_word = choice(secret_words_list)
attempts = 0
correct_letters = []

'''  FUNCTIONS  '''
def validate_guess():
    guess = input("Enter a letter (0 to exit): ").lower()
    while len(guess) != 1 or not guess.isalpha():
        guess = input("Enter a single letter: ").lower()
    return guess

def update_correct_letters(guess):
    if guess in secret_word:
        correct_letters.append(guess)
    return correct_letters

def get_masked_word():   
    masked_word = ""
    for letter in secret_word:
        if letter in correct_letters:
            masked_word += letter
        else:
            masked_word += "*"  
    return masked_word

def print_game_results():
    print(f"Attempts: {attempts}")
    if masked_word == secret_word:
        print("You win!" \
            f"The secret word is: {secret_word}")
    else:
        print("You lose!")
        print(f"The secret word is {secret_word}")



'''  MAIN PROGRAM  '''
print("*"*34)
print("LET'S PLAY THE WORD GUESSING GAME!")
print("*"*34)

while True:
    guess = validate_guess()

    if guess == "0":
        break

    correct_letters = update_correct_letters(guess)
    masked_word = get_masked_word()
    print(masked_word)

    attempts += 1

    if masked_word == secret_word:
        print_game_results()
        correct_letters.clear()
        attempts = 0
        secret_word = choice(secret_words_list)
        continue_playing = input("Do you want to play another round? Enter Y to keep playing: ").lower()

        if  continue_playing == "y":
            print("*"*34)
            print("LET'S PLAY THE WORD GUESSING GAME!")
            print("*"*34)
            continue
        else:
            break

        
