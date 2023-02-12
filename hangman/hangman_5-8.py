import random
words = ['python', 'java', 'swift', 'javascript']

def check_attempts(picked_word, hide_word, attempt):
    if attempt == 0:
        return print("\nThanks for playing!")

    word = list(hide_word)
    print(hide_word)
    user_input = input("Input a letter:")
    matches = []
    if user_input in picked_word:
        for i, el in enumerate(picked_word):
            if user_input == el:
                word[i] = el
        for l in matches:
            word[l[0]] = l[1]
    elif len(matches) == 0:
        print("That letter doesn't appear in the word.\n")
        return check_attempts(picked_word, hide_word, attempt - 1)

    hide_word = "".join(word)
    print(f'\n{hide_word}')
    return check_attempts(picked_word, hide_word, attempt - 1)
    

def main():
    picked_word = random.choice(words)
    hide_word = "-" * len(picked_word)
    print("H A N G M A N\n")
    check_attempts(picked_word, hide_word, 8) #initial number of attempts


if __name__ == '__main__':
    main()