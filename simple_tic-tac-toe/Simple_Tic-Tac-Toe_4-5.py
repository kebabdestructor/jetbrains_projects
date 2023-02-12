# Simple tic tac toe, stage 3/5

#Remove cells to find out winning combination
def check_winner(cells):
    combinations = {
            'h1': [(0, 0), (0, 1), (0, 2)],
            'h2': [(1, 0), (1, 1), (1, 2)],
            'h3': [(2, 0), (2, 1), (2, 2)],
            'v1': [(0, 0), (1, 0), (2, 0)],
            'v2': [(0, 1), (1, 1), (2, 1)],
            'v3': [(0, 2), (1, 2), (2, 2)],
            'd1': [(0, 0), (1, 1), (2, 2)],
            'd2': [(0, 2), (1, 1), (2, 0)]
    }

    for cell in cells:
        for key in combinations:
            if cell in combinations[key]:
                combinations[key].remove(cell)

    for key in combinations:
        if len(combinations[key]) == 0:
            return True
    return False

# Define occupied cells 
def find_positions(symbol, matrix):
    positions = []
    for h, row in enumerate(matrix):
        for v, el in enumerate(row):
            if el == symbol:
                positions.append((h, v))
    return positions


def check_cells(matrix):
    x_cells = find_positions('X', matrix) #cells occupied by X
    o_cells = find_positions('O', matrix) #cells occupied by O
    empty_cells = find_positions('_', matrix)

    x_winner = check_winner(x_cells) 
    o_winner = check_winner(o_cells)

    # check if there are a lot more X's than O's or vice versa
    if abs(len(x_cells) - len(o_cells)) > 1: 
        return print("Impossible")
    elif x_winner and o_winner:
        return print("Impossible")
    elif (not x_winner and not o_winner) and len(empty_cells) == 0:
        return print("Draw")
    elif (not x_winner and not o_winner) and len(empty_cells) >= 1:
        return print("Game not finished")
    elif x_winner:
        return print("X wins")
    elif o_winner:
        return print("O wins")

def check_user_turn(matrix):
    try:
        user_turn = tuple([int(x)-1 for x in input().split()])
    except ValueError:
        print("You should enter numbers!")
        return check_user_turn(matrix)

    for el in user_turn:
        if el > 2:
            print("Coordinates should be from 1 to 3!")
            return check_user_turn(matrix)

    empty_cells = find_positions('_', matrix)
    if user_turn not in empty_cells:
        print("This cell is occupied! Choose another one!")
        return check_user_turn(matrix)

    a, b = user_turn[0], user_turn[1]
    matrix[a][b] = 'X'
    flat_array = [item for sub_array in matrix for item in sub_array]
    print_grid(flat_array)


#Printing current grib
def print_grid(cells): 
    border = "-" * 9
    print(border + (3 * "\n| {} {} {} |").format(*cells) + "\n" + border)

def main():
    layout = input()
    array = list(layout)
    matrix = []  
    print_grid(array)   
    for i in range(0, 9, 3):
        matrix.append(array[i:i+3])
    
    check_user_turn(matrix)
    #check_cells(matrix)

if __name__ == '__main__':
    main()