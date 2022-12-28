import string
import random

def bot_move(name):
    if name == "Jack":
        return True
    return False

def find_move(pencils):
    if pencils == 1:
        return 1
    elif pencils % 4 == 0:
        return 3
    elif pencils % 4 == 3:
        return 2
    elif pencils % 4 == 2:
        return 1
    else:
        return random.randint(1, 3)

def check_pencils(pencils):
    try:
        number = int(pencils)
        if number <= 0:
            print("The number of pencils should be positive")
            return check_pencils(input())
        return number
    except:
        print("The number of pencils should be numeric")
        return check_pencils(input())

def check_name(name):
    if name == "John" or name == "Jack":
        return name
    else:
        print("Choose between 'John' and 'Jack'")
        return check_name(input())

def check_number(number, pencils):
    possible_numbers = ['1', '2', '3']
    if number not in possible_numbers:
        print("Possible values: '1', '2' or '3'")
        return check_number(input(), pencils)
    elif int(number) > pencils:
        print("Too many pencils were taken")
        return check_number(input(), pencils)
    return int(number)
    
def main():
    print("How many pencils would you like to use:")
    pencils = check_pencils(input())

    print("Who will be the first (John, Jack):")
    name = check_name(input())

    print("|" * pencils)
         
    while pencils > 0:
        print(f"{name}'s turn:")

        bot = bot_move(name)
        pencils_to_grab = 0
        if bot:
            pencils_to_grab = find_move(pencils)
            print(pencils_to_grab)
        else:
            pencils_to_grab = check_number(input(), pencils)

        if name == "John":
            name = "Jack"
        else:
            name = "John"
        
        pencils = pencils - int(pencils_to_grab)
        if pencils == 0:
            print(f"{name} won!")
            break
        
        print("|" * pencils) 
    
main()

