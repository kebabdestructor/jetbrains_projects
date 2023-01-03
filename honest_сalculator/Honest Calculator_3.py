msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):" 
msg_5 = "Do you want to continue calculations? (y / n):"

memory = 0.0

def check_input():
    print(msg_0)
    try:
        x, oper, y = input().split()
    except ValueError:
        print('Wrong number of input values, there should be 3')
    else:
        if x == 'M': x = memory
        elif y == 'M': y = memory
        check_values(x, oper, y)

def check_values(x, oper, y):
    try:
        x = float(x)
        y = float(y)
    except ValueError:
        print(msg_1)
        check_input()
    else:
        check_operator(x, oper, y)
        
def check_operator(x, oper, y):
    valid_operators = ['+', '-', '*', '/']
    if oper in valid_operators:
        if oper == '/' and y == 0:
            print(msg_3)
            check_input()
        else:
            calculate(x, oper, y)
    else:
        print(msg_2)
        check_input()

def calculate(x, oper, y):
    result = 0
    match oper:
        case "+": result = x + y
        case "-": result = x - y
        case "*": result = x * y
        case "/": result = x / y

    print(result)
    save_result(result)

def save_result(result):
    global memory
    print(msg_4)
    answer_store_result = input()
    if answer_store_result == 'y':
        memory = result
    print(msg_5)
    answer_continue_calc = input()
    if answer_continue_calc == 'y':
        check_input()

check_input()