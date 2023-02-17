import string
import random_word

word = random_word.RandomWords().get_random_word()
word = ''.join(filter(lambda c: c.islower(), word))

body_parts = [
    " O\n/", "|", "\\\n/", " |", "\n^"
]


def display_body(lives):
    if lives < len(body_parts):
        return "".join(body_parts[:lives])
    else:
        return "".join(body_parts)


def display_word(word, guessed_letters):
    result = ""
    for letter in word:
        if letter in guessed_letters:
            result += letter + " "
        else:
            result += "_ "
    return result.strip()


while True:
    lives = 9
    guessed_letters = set()

    while True:
        print(display_body(lives))
        print(display_word(word, guessed_letters))

        if set(word) <= guessed_letters:
            print("You win!")
            break
        elif lives == 0:
            print("You lose! The word was", word)
            break

        guess = input("Guess a letter: ").lower()

        if guess not in string.ascii_lowercase:
            print("Invalid input! Please enter a letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        if guess in word:
            guessed_letters.add(guess)
            print("Correct!")
        else:
            lives -= 1
            print("Incorrect!")
    break
