import math

def months_to_pay(principal, payment):
    months = math.ceil(principal / payment)
    return months 

def calulate_payment(principal, months):
    payment = math.ceil(principal / months)
    lastpayment = principal - ((months - 1) * payment)
    return (payment, lastpayment)

def check_input_options(option, principal):
    if option == 'p':
        print("Enter the number of months:")
        months = int(input())
        payment, lastpayment = calulate_payment(principal, months)
        if lastpayment != 0:
            print(f"Your monthly payment = {payment} and the last payment = {lastpayment}")  
        else:
            print(f"Your monthly payment = {payment}")

    if option == 'm':
        print("Enter the monthly payment:")
        monthly_payment = int(input())
        months = months_to_pay(principal, monthly_payment)
        if months == 1:
            print("It will take 1 month to repay the loan")
        else:
            print(f"It will take {months} months to repay the loan")

def main():
    print("Enter the loan principal:")
    loan_principal = int(input())
    print("""What do you want to calculate?
            type "m" - for number of monthly payments,
            type "p" - for the monthly payment:""")
    check_input_options(input(), loan_principal)

main()