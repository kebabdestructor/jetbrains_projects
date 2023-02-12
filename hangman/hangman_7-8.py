import random
words = ['python', 'java', 'swift', 'javascript']

def check_user_input(hint):
    print(f'\n{hint}')
    user_input = input("Input a letter: ")
    if  len(user_input) > 1 or user_input == "":
        print("Please, input a single letter")
        return check_user_input(hint)
    if user_input.isupper() or not (user_input.isalpha()):
        print("Please, enter a lowercase letter from the English alphabet.")
        return check_user_input(hint)
    if user_input in hint:
        print("You've already guessed this letter.")
        return check_user_input(hint)
    else:
        return user_input

def check_attempts(picked_word, hint, attempt):
    if hint == picked_word:
        return print(f"You guessed the word {picked_word}!\nYou survived!")
    if attempt == 0:
        return print("\nYou lost!")

    word = list(hint)
    
    user_input = check_user_input(hint)

    if user_input in picked_word:
        for i, el in enumerate(picked_word):
            if user_input == el:
                word[i] = el
        return check_attempts(picked_word, "".join(word), attempt)
    elif user_input not in picked_word:
        print(f"That letter doesn't appear in the word.")
        return check_attempts(picked_word, hint, attempt - 1)


def main():
    picked_word = random.choice(words)
    hint = "-" * len(picked_word)
    print("H A N G M A N")
    check_attempts(picked_word, hint, 8) #initial number of attempts


if __name__ == '__main__':
    main()