# Write your code here
import random


winning_combinations = {'scissors': 'rock', 'rock': 'paper', 'paper': 'scissors'}
combinations = ['scissors', 'rock', 'paper']

def play_game(user_input):
    if user_input not in combinations and user_input != '!exit':
        print("Invalid input")
        return play_game(input())
    elif user_input == '!exit':
        print('Bye!')
        return
    random_choice = random.choice(combinations)
    if random_choice == user_input:
        print(f'There is a draw ({user_input})')
    elif winning_combinations[user_input] == random_choice:
        print(f'Sorry, but the computer chose {random_choice}')
    else:
        print(f'Well done. The computer chose {random_choice} and failed')
    return play_game(input())

play_game(input())