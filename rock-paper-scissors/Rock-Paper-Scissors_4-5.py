# Write your code here
import random

friends = {}
player = input("Enter your name: ")
print(f"Hello, {player}")
if player not in friends:
    friends[player] = 0

with open("rock-paper-scissors\\rating.txt", "r") as f:
    for line in f:
        name, rating = line.strip().split(" ")
        friends[name] = int(rating)

winning_combinations = {'scissors': 'rock', 'rock': 'paper', 'paper': 'scissors'}
combinations = ['scissors', 'rock', 'paper']

def play_game(user_input, player):
    print(user_input, player)
    if user_input == '!rating':
        print(f'Your rating: {friends[player]}')
        return play_game(input(), player)
    elif user_input == '!exit':
        print('Bye!')
        return
    elif user_input not in combinations:
        print("Invalid input")
        return play_game(input(), player)
    random_choice = random.choice(combinations)
    if random_choice == user_input:
        print(f'There is a draw ({user_input})')
        friends[player] += 50
    elif winning_combinations[user_input] == random_choice:
        print(f'Sorry, but the computer chose {random_choice}')
    else:
        print(f'Well done. The computer chose {random_choice} and failed')
        friends[player] += 100
    return play_game(input(), player)

play_game(input(), player)