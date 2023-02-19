import random

class Dominoes:
    
    def __init__(self):
        self.initial_stock_pieces = [[i, j] for i in range(7) for j in range(i, 7)]
        self.stock_pieces = []
        self.computer_pieces = []
        self.player_pieces = []
        self.domino_snake = []
        self.status = 'start_game'
        self.game_result = 'none'

    def display_output(self):
        reduced_snake = self.domino_snake.copy()
        snake = ''
        output = ''
        if len(self.domino_snake) >= 7:
            reduced_snake = self.domino_snake[0:3] + self.domino_snake[-3:]

        for indx, item in enumerate(reduced_snake):
            if len(self.domino_snake) > 6 and indx == 3:
                snake += '...' + str(item)
            else:
                snake += str(item)

        print("=" * 70)
        print(f"Stock size: {len(self.stock_pieces)}")
        print(f"Computer pieces: {len(self.computer_pieces)}\n")
        print(f"{snake}\n")
        print("Your pieces:")

        for indx, pieces in enumerate(self.player_pieces):
            output += f'{indx+1}: {pieces}\n'

        if self.game_result == 'draw':
            output += "\nStatus: The game is over. It's a draw!"
        elif self.game_result == 'computer':
            output += "\nStatus: The game is over. The computer won!"
        elif self.game_result == 'player':
            output += "\nStatus: The game is over. You won!"
        elif self.status == 'computer':
            output += "\nStatus: Computer is about to make a move. Press Enter to continue..."
        elif self.status == 'player':
            output += "\nStatus: It's your turn to make a move. Enter your command."
        print(output)

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
            elif piece in player_pieces:
                self.player_pieces.remove(piece)
                self.domino_snake.append(piece)
                self.status = 'computer'

    def check_user_input(self, user_input):
        try:
            user_input = int(user_input)
            if abs(user_input) > len(self.player_pieces):
                print("Invalid input. Please try again.")
                return self.check_user_input(input())
        except ValueError:
            print("Invalid input. Please try again.")
            return self.check_user_input(input())
        else:
            return user_input

    def add_piece_to_snake(self, user_input, removed_piece):
        if user_input < 0:
            self.domino_snake.insert(0, removed_piece)
        elif user_input > 0:
            self.domino_snake.append(removed_piece)

    def take_domino_from_stock(self):
        if len(self.stock_pieces) > 0:
            return self.stock_pieces.pop()
        else:
            return None

    def check_selected_piece(self, selected_piece, pieces, side=0):
        snake_head = self.domino_snake[0]
        snake_tail = self.domino_snake[-1]
        match = None
        if side <= 0:
            if snake_head[0] in selected_piece:
                if selected_piece[1] == snake_head[0]:
                    match = (selected_piece, -1)
                else:
                    match = (selected_piece[::-1], -1)
        if side >= 0:
            if snake_tail[1] in selected_piece:
                if selected_piece[0] == snake_tail[1]:
                    match = (selected_piece, 1)
                else:
                    match = (selected_piece[::-1], 1)
        if match:
            self.add_piece_to_snake(match[1], match[0])
            pieces.remove(selected_piece)
            return True
        else:
            return False

    def handle_player_move(self):
        user_input = self.check_user_input(input())
        if user_input == 0:
            taken_piece = self.take_domino_from_stock()
            if taken_piece:
                self.player_pieces.append(taken_piece)
        else:
            selected_piece = self.player_pieces[abs(user_input) - 1]
            correct_piece = self.check_selected_piece(selected_piece, self.player_pieces, user_input)
            if not correct_piece:
                print('Illegal move. Please try again.')
                return self.handle_player_move()
    
    def make_best_move(self, score_results):
        score_list = sorted(list(score_results.keys()), reverse=True)
        for score in score_list:
            for piece in score_results[score]:
                if self.check_selected_piece(piece, self.computer_pieces):
                    return
        else:
            return 0    

    def find_best_move(self):
        joined_pieces = self.computer_pieces + self.domino_snake
        unpack_list = [el for subarr in joined_pieces for el in subarr]
        num_occurences = dict.fromkeys([i for i in range(7)], 0)
        for el in unpack_list:
            num_occurences[el] = num_occurences[el] + 1
        
        score_results = {}
        for piece in self.computer_pieces:
            score = num_occurences[piece[0]] + num_occurences[piece[1]]
            if score in score_results:
                score_results[score].append(piece)
            else:
                score_results.update({score: [piece]})
        return score_results

    def handle_computer_move(self, user_input=''):
        scores = self.find_best_move()
        selected_piece = self.make_best_move(scores)
        if selected_piece != 0:
            return
        else:
            taken_piece = self.take_domino_from_stock()
            if taken_piece:
                self.computer_pieces.append(taken_piece)


    def check_game_result(self, pieces):
        number_at_ends = self.domino_snake[0][0]
        unpacked_list = [el for subarr in self.domino_snake for el in subarr]
        max_occurences = max(unpacked_list, key=unpacked_list.count)
        if len(pieces) == 0:
            self.game_result = self.status
        elif self.domino_snake[0][0] == self.domino_snake[-1][1]:
            if unpacked_list.count(number_at_ends) == 8:
                self.game_result = self.status
        elif unpacked_list.count(max_occurences) == 8:
            self.game_result = 'draw'
        

    def main(self):
        if self.game_result != 'none':
            exit()
        elif self.status == 'start_game':
            self.shuffle_dominoes()
            self.split_domino_set()
            self.find_starting_domino()
            self.display_output()
        elif self.status == "player":
            self.handle_player_move()
            self.check_game_result(self.player_pieces)
            self.status = "computer"
            self.display_output()
        elif self.status == "computer":
            self.handle_computer_move(input())
            self.check_game_result(self.computer_pieces)
            self.status = "player"
            self.display_output()
        return self.main()

game = Dominoes()
game.main()


