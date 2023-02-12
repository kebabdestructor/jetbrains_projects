import random
words = ['python', 'java', 'swift', 'javascript']

def check_user_input(hint, used_letters):
    print(f'\n{hint}')
    user_input = input("Input a letter: ")
    if  len(user_input) > 1 or user_input == "":
        print("Please, input a single letter")
        return check_user_input(hint, used_letters)
    if user_input.isupper() or not (user_input.isalpha()):
        print("Please, enter a lowercase letter from the English alphabet.")
        return check_user_input(hint, used_letters)
    if user_input in used_letters:
        print("You've already guessed this letter.")
        return check_user_input(hint, used_letters)
    else:
        used_letters.add(user_input)
        return user_input

def play_game(picked_word, hint, attempt, score, used_letters):
    if hint == picked_word:
        print(f"You guessed the word {picked_word}!\nYou survived!")
        score[0] += 1
        return main(score)
    if attempt == 0:
        score[1] += 1
        print("\nYou lost!")
        return main(score)

    word = list(hint)
    
    user_input = check_user_input(hint, used_letters)

    if user_input in picked_word:
        for i, el in enumerate(picked_word):
            if user_input == el:
                word[i] = el
        return play_game(picked_word, "".join(word), attempt, score, used_letters)
    elif user_input not in picked_word:
        print(f"That letter doesn't appear in the word.")
        return play_game(picked_word, hint, attempt - 1, score, used_letters)


def main(score=[0, 0]):
    won, lost = score
    option = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ')
    match option:
        case 'play':
            picked_word = random.choice(words)
            hint = "-" * len(picked_word)
            play_game(picked_word, hint, 8, score, set()) #initial number of attempts 8
        case 'results':
            print(f"You won: {won} times.")
            print(f"You lost: {lost} times.")
            return main()
        case 'exit':
            return
        case default:
            return main()

if __name__ == '__main__':
    print("H A N G M A N")
    main()