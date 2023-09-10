import random

def random_word():
    words = ["play", "letter", "ball", "city", "islamabad", "shahrukh"]
    return random.choice(words)

def display_word(word, guess):
    display = ""
    for letter in word:
        if letter in guess:
            display += letter
        else:
            display += "_"
    return display
def hangman():
    max_attempts = 6
    word_to_guess = random_word()
    guess = []

    print("welcome to hangman!")
    print(display_word(word_to_guess, guess))

    while max_attempts > 0:
        guessed = input("guess a letter: ").lower()
        if len(guessed) != 1 or not guessed.isalpha():
            print("invalid input: try again!")
            continue
        if guessed in guess:
            print("You already guessed this letter. Try again.")
            continue
        guess.append(guessed)

        if guessed in word_to_guess:
            print("CORRECT!")
        else:
            max_attempts -= 1
            print(f"wrong! you have {max_attempts} attempts left")
        print(display_word(word_to_guess, guess))
        if "_" not in display_word(word_to_guess, guess):
            print("CONGRATULATIONS! you guessed the word right!")
            break

    if max_attempts== 0:
        print("no attempts left, the word was: ", word_to_guess)

if __name__ == "__main__":
    hangman()