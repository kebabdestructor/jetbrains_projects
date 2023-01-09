import math
import string
import argparse

parser = argparse.ArgumentParser(description="Use Loan Calculator to calculate: annuity payment, differentiated payments, principal loan with overpayment")
parser.add_argument("--type", choices=["annuity", "diff"], help="You need to choose either annuity or differentiated payment.")
parser.add_argument("--payment", type=float)
parser.add_argument("--principal", type=float)
parser.add_argument("--periods", type=int)
parser.add_argument("--interest", type=float)

args = parser.parse_args()
parameters = [args.type, args.payment, args.principal, args.periods, args.interest]


def check_invalid_parameters(parameters):
    if args.type is None or args.interest is None:
        return [False, False]

    if args.type == "diff" and args.payment is not None:
        return [False, False]

    null_indx = [indx for indx, item in enumerate(parameters) if item is None] #find out what value is None
    if len(null_indx) > 1:
        return [False, False]

    null_indx = null_indx.pop() #converting from list to sting
    parameters.pop(null_indx) #remove indexes that is None

    negative_values = [item for item in parameters[1:] if item < 0] #find out what value is less than 0
    if len(negative_values) > 0:
        return [False, False]   
    else:
        return [parameters, null_indx]

def calculate_diff(diff_parameters):
    P, n, i = diff_parameters
    total = 0
    for m in range(1, n + 1):
        D = math.ceil(P / n + i * (P - ((P * (m - 1)) / n)))
        total += D
        print(f"Month {m}: payment is {D}")
    Overpayment = (total - P)
    print(f"\nOverpayment = {Overpayment}")

def  calculate_annuity_payment(annuity_parameters):
    P, n, i = annuity_parameters
    A = math.ceil(P * (i * pow((1 + i), n) / (pow((1 + i), n) - 1)))
    Overpayment = ((A * n) - P)
    print(f"Your annuity payment = {A}!")
    print(f"Overpayment = {int(Overpayment)}")

def calculate_annuity_principal(annuity_parameters):
    A, n, i = annuity_parameters
    P = math.floor(A / ((i * pow((1 + i), n)) / (pow((1 + i), n) - 1)))
    print(f"Your loan principal = {P}!")
    print(f"Overpayment = {math.ceil((A * n) - P)}")

def calculate_annuity_period(annuity_parameters):
    A, P, i = annuity_parameters
    x = (A / (A - i * P))
    n = math.log(x, i + 1)
    n = math.ceil(n)
    print('It will take',
          f'{n} months' if n < 12
          else (f'{int(n // 12)} year' if n % 12 == 0
                else f'{int(n // 12)} years and {math.ceil(n % 12)} months'),
          'to repay this loan!')
    print(f"Overpayment = {(A * n) - P}")


def check_args(parameters):
    validated_parameters, null_indx = check_invalid_parameters(parameters)
    if validated_parameters == False: 
        return print("Incorrect parameters")

    validated_parameters[3] = validated_parameters[3] / (12 * 100) # convert yearly interest rate to monthly

    if args.type == 'diff':
        calculate_diff(validated_parameters[1:])
    elif args.type == 'annuity':
        if null_indx == 1: 
            calculate_annuity_payment(validated_parameters[1:]) #remove 0 index that corresponds to args.type.
        elif null_indx == 2: 
            calculate_annuity_principal(validated_parameters[1:])
        elif null_indx == 3:
            calculate_annuity_period(validated_parameters[1:])

check_args(parameters)