# Write your code here
import random

class Rock_Paper_Scissors:

    def __init__(self):
        self.friends = {}
        self.status = ''
        self.player = ''
        self.mode = ''
        self.comp_choice = ''
        self.combinations = ['scissors', 'rock', 'paper']
        self.classic_combinations = {'scissors': 'rock', 'rock': 'paper', 'paper': 'scissors'}


    def start_game(self):
        player = input("Enter your name: ")
        self.player = player
        print(f"Hello, {self.player}")
        with open("rock-paper-scissors\\rating.txt", "r") as f:
            for line in f:
                name, rating = line.strip().split(" ")
                self.friends[name] = int(rating)
        if self.player not in self.friends:
            self.friends[self.player] = 0

        combinations = input()
        if combinations == "":
            self.mode = 'classic'
        else:
            self.mode = 'custom'
            self.combinations = combinations.split(',')
        print("Okay, let's start")

    def display_winner(self, winner):
        if winner == 'draw':
            print(f'There is a draw ({self.status})')
            self.friends[self.player]  += 50
        elif winner == 'computer':
            print(f'Sorry, but the computer chose {self.comp_choice}')
        else:
            print(f'Well done. The computer chose {self.comp_choice} and failed')
            self.friends[self.player] += 100

    def play_classic(self):
        winner = ''
        if self.comp_choice == self.status:
            winner = "draw"
        elif self.classic_combinations[self.status] == self.comp_choice:
            winner = "computer"
        else:
            winner = "player"
        return self.display_winner(winner)

    def play_custom(self):
        winner = ''
        item_indx = self.combinations.index(self.status)
        combinations = self.combinations.copy()
        combinations.remove(self.status)

        new_combinations = combinations[item_indx:] + combinations[:item_indx]
        divide_point = len(new_combinations) // 2

        winner_combinations = new_combinations[:divide_point]
        loser_combinations = new_combinations[divide_point:]

        if self.comp_choice == self.status:
            winner = 'draw'
        elif self.comp_choice in loser_combinations:
            winner = 'player'
        elif self.comp_choice in winner_combinations:
            winner = 'computer'
        return self.display_winner(winner)

    def find_winner(self):
        self.comp_choice = random.choice(self.combinations)
        if self.mode == 'classic':
            return self.play_classic()
        elif self.mode == 'custom':
            return self.play_custom()

    def main(self, status):
        self.status = status
        if status == 'start':
            self.start_game()
        elif status == "!rating":
            print(f'Your rating: {self.friends[self.player]}')
        elif status == "!exit":
            print('Bye!')
            exit()
        elif status not in self.combinations:
            print("Invalid input")
        elif status in self.combinations:
            self.find_winner()
        return self.main(input())

new_player = Rock_Paper_Scissors()
new_player.main('start')