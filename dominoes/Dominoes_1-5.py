import random

class Dominoes:
    
    def __init__(self):
        self.initial_stock_pieces = [[i, j] for i in range(7) for j in range(i, 7)]
        self.stock_pieces = []
        self.computer_pieces = []
        self.player_pieces = []
        self.domino_snake = []
        self.status = 'none'

    def __str__(self):
        return f'Stock pieces: {self.stock_pieces}\n' \
            f'Computer pieces: {self.computer_pieces}\n' \
            f'Player pieces: {self.player_pieces}\n' \
            f'Domino snake: {self.domino_snake}\n' \
            f'Status: {self.status}'
        
    def shuffle_dominoes(self):
        random.shuffle(self.initial_stock_pieces)

    def split_domino_set(self):
        self.stock_pieces = self.initial_stock_pieces[0:14]
        self.player_pieces = self.initial_stock_pieces[14:21]
        self.computer_pieces = self.initial_stock_pieces[21:28]

    def find_starting_domino(self):
        computer_pieces = [el for el in self.computer_pieces if el[0] == el[1]]
        player_pieces = [el for el in self.player_pieces if el[0] == el[1]]
        double_pieces = computer_pieces + player_pieces
        if double_pieces:
            piece = max(double_pieces)
            if piece in computer_pieces:
                self.computer_pieces.remove(piece)
                self.domino_snake.append(piece)
                self.status = 'player'
                return True
            elif piece in player_pieces:
                self.player_pieces.remove(piece)
                self.domino_snake.append(piece)
                self.status = 'computer'
                return True
        else:
            return False

    def main(self):
        self.shuffle_dominoes()
        self.split_domino_set()
        if not self.find_starting_domino():
            self.main()
        else:
            print(self)

game = Dominoes()
game.main()
