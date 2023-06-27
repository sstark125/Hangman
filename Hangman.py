import random
import os
from hangman_words import word_list
def ConsoleClear():
    os.system('cls' if os.name == 'nt' else 'clear')
ConsoleClear() 

# word_list = ["aardvark", "baboon", "camel"]

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
print("Welcome to Hangman")

playGame = int(input("1. Play\n2. Exit\n"))
ConsoleClear()
# Checks whether user decided to play
while playGame != 2:
    chosen_word = random.choice(word_list)
    # Creates version of chosen word displaying only underscores
    display = []
    for letter in chosen_word:
        display.append("_")
    newDisplay = ''.join(str(item) for item in display)
    print(stages[6])
    print(newDisplay)

    # instantiate variables for game
    lives = 6
    guessedWord = 0
    guessedLetters = []
    guess = input("Guess a letter: ").lower()
    
    art = 6
    while lives > 0 and guessedWord < len(chosen_word):
        ConsoleClear()
        correct = 0
        # Checks to see if letter has already been guessed
        if guess not in guessedLetters:
            for letter in chosen_word:
                if guess == letter:
                    for letter in range(len(chosen_word)):
                        if guess == chosen_word[letter]:
                            display[letter] = guess
                    correct += 1
                    guessedWord += 1

            if correct == 0:
                lives -= 1

            if lives != 0 and guessedWord < len(chosen_word):
                guessedLetters.append(guess)
                ConsoleClear()
                newDisplay = ''.join(str(item) for item in display)
                print(stages[lives])
                print(newDisplay)
                print(f"Lives: {lives}")
                guess = input("Guess a letter: ").lower()
        else:
            ConsoleClear()
            print("You already picked that letter")
            newDisplay = ''.join(str(item) for item in display)
            print(stages[lives])
            print(newDisplay)
            print(f"Lives: {lives}")
            guess = input("Guess a letter: ").lower()

    if lives == 0:
        ConsoleClear()
        print(stages[lives])
        print(f"The word was: {chosen_word}")
        print("You lost")
    else:
        ConsoleClear()
        print(stages[lives])
        print(f"The word was: {chosen_word}")
        print("You got it!")
        print("")

    playGame = int(input("\n1. Play Again\n2. Exit\n"))
    ConsoleClear()