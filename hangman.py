import random
import hangman_art
import hangman_words
word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
lives = 6
end_of_game = False
guess = ""
display = []

print(hangman_art.logo)
#print(f"Passt, the solution is {chosen_word}")

for letter in chosen_word:
    display += "_"
print(display)

while not end_of_game:
    user_quess = input("Guess a letter: ").lower()

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        # print(f"Current position: {position}\nCurrent letter: {letter}\n Guessed letter: {user_quess}")
        if user_quess == letter:
            display[position] = letter

    if user_quess not in chosen_word:
        lives -= 1
        print(f"You guessed {user_quess}, that's not in the word. You lose a life.")
        
        if lives == 0:
            print(f"You lose! Chosen word is {chosen_word}")
            end_of_game = True

    print("".join(display))
    if "_" not in display:
        end_of_game = True
        print("You win!")

    print(hangman_art.stages[lives])