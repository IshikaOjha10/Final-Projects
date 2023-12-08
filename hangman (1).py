import random

from words import words

def choose_word(word_list):
    if not word_list:
        return None
    word = random.choice(word_list)
    word_list.remove(word)
    return word

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]

def hangman():

    used_words = []
    play_again = "yes"

    print("Welcome to Hangman!")
    print("Hint: The word is a fruit name")

    while play_again.lower() == "yes" and words:
        word_to_guess = choose_word(words)
        guessed_letters = []
        attempts = 6

        while attempts > 0:
            print(display_word(word_to_guess, guessed_letters))
            guess = input("Guess a letter: ").lower()

            if guess in guessed_letters:
                print("You've already guessed that letter.")
            elif guess in word_to_guess:
                print("Good guess!")
                guessed_letters.append(guess)
                if display_word(word_to_guess, guessed_letters) == word_to_guess:
                    print(f"Congratulations! You've guessed the word: {word_to_guess}")
                    break
            else:
                print("Wrong guess.")
                guessed_letters.append(guess)
                attempts -= 1
                print(f"Attempts left: {attempts}")
                print(display_hangman(6 - attempts))

        if attempts == 0:
            print(f"Sorry, you're out of attempts. The word was: {word_to_guess}")

        if words:
            play_again = input("Do you want to play again? (yes/no): ")
        else:
            print("No more words to guess.")

if __name__ == "__main__":
    hangman()
