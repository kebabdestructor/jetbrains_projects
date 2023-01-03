msgs = {
    0: "Enter an equation", 
    1: "Do you even know what numbers are? Stay focused!", 
    2: "Yes ... an interesting math operation. You've slept through all classes, haven't you?", 
    3: "Yeah... division by zero. Smart move...", 
    4: "Do you want to store the result? (y / n):", 
    5: "Do you want to continue calculations? (y / n):", 
    6: " ... lazy", 
    7: " ... very lazy", 
    8: " ... very, very lazy", 
    9: "You are", 
    10: "Are you sure? It is only one digit! (y / n)", 
    11: "Don't be silly! It's just one number! Add to the memory? (y / n)", 
    12: "Last chance! Do you really want to embarrass yourself? (y / n)"}

memory = 0.0

def check_input():
    print(msgs[0])
    try:
        x, oper, y = input().split()
    except ValueError:
        print('Wrong number of input values, there should be 3')
    else:
        if x == 'M': x = memory
        if y == 'M': y = memory
        check_values(x, oper, y)

def check_values(x, oper, y):
    try:
        x = float(x)
        y = float(y)
    except ValueError:
        print(msgs[1])
        check_input()
    else:
        check_operator(x, oper, y)
        
def check_operator(x, oper, y):
    valid_operators = ['+', '-', '*', '/']
    if oper in valid_operators:
        check(x, y, oper)
        if oper == '/' and y == 0:
            print(msgs[3])
            check_input()
        else:
            calculate(x, oper, y)
    else:
        print(msgs[2])
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
    print(msgs[4])
    answer_store_result = input()
    if answer_store_result == 'y':
        store_in_memory(result, 10)
    print(msgs[5])
    answer_continue_calc = input()
    if answer_continue_calc == 'y':
        check_input()

def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + msgs[6]
    if (v1 == 1 or v2 == 1) and v3 == '*':
        msg = msg + msgs[7]
    if (v1 == 0 or v2 == 0) and (v3 == '*' or v3 == "+" or v3 == "-"):
        msg = msg + msgs[8]
    if msg != '':
        msg = msgs[9] + msg
        print(msg)
    
def is_one_digit(v):
    if v > -10 and v < 10 and v.is_integer():
        return True
    return False

def store_in_memory(result, msg_index_value):
    global memory
    if not is_one_digit(result):
        memory = result
        return 
    
    msg_index = msg_index_value
    print(msgs[msg_index])
    answer = input()
    if answer == 'y':
        if msg_index < 12:
            msg_index += 1
            store_in_memory(result, msg_index)
        else:
            memory = result
    elif answer == 'n':
        return
    else:
        store_in_memory(result, msg_index)


check_input()