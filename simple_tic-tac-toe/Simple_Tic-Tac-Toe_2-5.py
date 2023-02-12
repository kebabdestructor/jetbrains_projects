# Simple tic tac toe, stage 2/5

def main():
    layout = input()
    array = list(layout)
    new_array = []
    c = 0   
    for i in range(3):
        new_array.append(array[c:c+3])
        new_array[i].insert(0, '|')
        new_array[i].insert(5, '|')
        c += 3

    for i, el in enumerate(new_array):
        if i == 0:
            print("---------")
        print(*el)
        if i == len(new_array) -1:
            print("---------")

if __name__ == '__main__':
    main()