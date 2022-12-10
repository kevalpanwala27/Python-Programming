# Step 3

import random

word_list = ["tiger", "lion", "donkey"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Testing code
print(f"Pssst, the solution is {chosen_word}.")

# Create Blanks
display = []
word_length = len(chosen_word)
for _ in range(len(word_length)):
    display += "_"

# TODO - 1 - Use a while loop to let the user guess again.
#  The loop should stop once the user has guessed all the letters in the chosen_word
#  and 'display' has no more blanks ("_"). Then you can tell the user they have won.

end_of_game = False

while not end_of_game:
    guess = input("Guess  letter: ").lower()

    # Check guessed letter
    for position in range(len(word_length)):
        letter = chosen_word[position]
        print(f"Current position: {position}\nCurrent letter: {letter}\nGuessed letter: {guess}")
        if letter == guess:
            display[position] = letter

print(display)

if "_" not in display:
    end_of_game = True
    print("You win.")





