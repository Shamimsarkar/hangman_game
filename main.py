import random

from hangman_words import word_list
from hangman_art import stages,logo

print(logo)

lives = 6

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
for position in range(len(chosen_word)):
    placeholder += "_"
print("Word to guess" + placeholder)

game_over = False
correct_letter = []

while not game_over:

    print(f"****************************{lives}/6 LIVES LEFT****************************")

    guess = input("Guess a letter: ").lower()

    display = ""

    if guess in correct_letter:
        print(f"You have already guess the letter {guess}")

    if guess not in chosen_word:
        lives -= 1
        print(f"You guess {guess}  which is not in Word.")

        if lives == 0:
            game_over = True
            print(f"***********************IT WAS {chosen_word}! YOU LOSE**********************")
            print("Sorry you lose the game")

    for letter in chosen_word:
        if guess == letter:
            display += letter
            correct_letter.append(guess)
        elif letter in correct_letter:
            display += letter
        else:
            display += "_"

    print(display)

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")
    print(stages[lives])