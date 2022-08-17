import random
from words import words
import string


def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 7

    while len(word_letters) > 0 and lives > 0:
        print('\nYou have', lives, 'lives left and used these letters:\n ', ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current Word: ', ' '.join(word_list),'\n')

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
              lives = lives - 1
              print('\n',user_letter,'is not in the word ')

        elif user_letter in used_letters:
            print('\nYou have already used',user_letter, 'Try Again')

        else:
            print('\nInvalid Character')
  
    if lives == 0:
        print('You Lost! the word was',word)
    else:
        print('You guessed the word', word, "!!!")
  
hangman()