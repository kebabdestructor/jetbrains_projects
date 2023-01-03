msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):" 
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"

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
        check(x, y, oper)
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

def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + msg_6
    if (v1 == 1 or v2 == 1) and v3 == '*':
        msg = msg + msg_7
    if (v1 == 0 or v2 == 0) and (v3 == '*' or v3 == "+" or v3 == "-"):
        msg = msg + msg_8
    if msg != '':
        msg = msg_9 + msg
        print(msg)
    
def is_one_digit(v):
    if v > -10 and v < 10 and v.is_integer():
        return True
    return False

check_input()