# Step 2

import random

word_list = ["tiger", "lion", "donkey"]
chosen_word = random.choice(word_list)

# Testing
print(f"Pssst, the solution is {chosen_word}")

# TODO - 1 - Create an empty list called Display. For each letter in the chosen_word, add a "_" to 'display'.So if
#  the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing letter to guess.

display = []
word_length = len(chosen_word)
for _ in range(len(word_length)):
    display += "_"
print(display)

guess = input("Guess  letter: ").lower()

# TODO - 2 - Loop through each position in the chosen_word;
# If the letter at that position matches 'guess' then reveal that letter in the display at that position.
# e.g. if the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

for position in range(len(word_length)):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter

# TODO - 3 - Print 'Display' and you should see the guessed letter in the correct position and every other letter
#  replace with "_".
# Hint - Don't worry about getting the user to guess the next letter . we'll tackle that in step 3.


