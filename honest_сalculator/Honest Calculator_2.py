msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."

def check_input():
    print(msg_0)
    try:
        x, oper, y = input().split()
    except ValueError:
        print('Wrong number of input values, there should be 3')
    else:
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

check_input()