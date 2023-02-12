import random
words = ['python', 'java', 'swift', 'javascript']

def check_attempts(picked_word, hide_word, attempt):
    if hide_word == picked_word:
        return print("You guessed the word!\nYou survived!")
    if attempt == 0:
        return print("\nYou lost!")

    word = list(hide_word)
    print(f'\n{hide_word}')
    user_input = input("Input a letter: ")

    if user_input in hide_word:
        print(f"No improvements. # {attempt -1} attempts")
        return check_attempts(picked_word, hide_word, attempt - 1)
    elif user_input in picked_word:
        for i, el in enumerate(picked_word):
            if user_input == el:
                word[i] = el
        return check_attempts(picked_word, "".join(word), attempt)
    elif user_input not in picked_word:
        print(f"That letter doesn't appear in the word.\n # {attempt -1} attempts")
        return check_attempts(picked_word, hide_word, attempt - 1)


def main():
    picked_word = random.choice(words)
    hide_word = "-" * len(picked_word)
    print("H A N G M A N")
    check_attempts(picked_word, hide_word, 8) #initial number of attempts


if __name__ == '__main__':
    main()