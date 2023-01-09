import math
import string

def calculate_monthly_payments(P, A, I):
    monthly_payment = 0
    i = I / (12 * 100)
    x = (A / (A - i * P))
    n = math.log(x, i + 1)
    n = math.ceil(n)
    print('You need',
          f'{n} months' if n < 12
          else (f'{int(n // 12)} year' if n % 12 == 0
                else f'{int(n // 12)} years and {math.ceil(n % 12)} months'),
          'to repay this credit!')
    print(monthly_payment)

def calculate_monthly_annuity(P, n, I):
    i = I / (12 * 100)
    A = P * (i * pow((1 + i), n) / (pow((1 + i), n) - 1))
    print(f"Your monthly payment = {math.ceil(A)}!")

def calculate_loan_principal(A, n, I):
    i = I / (12 * 100)
    P = A / ((i * pow((1 + i), n)) / (pow((1 + i), n) - 1))
    print(f"Your loan principal = {math.ceil(P)}!")


def check_input_options(option):
    if option == 'n':
        loan_principal = float(input("Enter the loan principal:\n"))
        monthly_payment = float(input("Enter the monthly payment:\n"))
        loan_interest = float(input("Enter the loan interest:\n"))
        calculate_monthly_payments(loan_principal, monthly_payment, loan_interest)

    elif option == 'a':
        loan_principal = float(input("Enter the loan principal:\n"))
        periods = float(input("Enter the number of periods:\n"))
        loan_interest = float(input("Enter the loan interest:\n"))
        calculate_monthly_annuity(loan_principal, periods, loan_interest)

    elif option == 'p':
        annuity_payment = float(input("Enter the annuity payment:\n"))
        periods = float(input("Enter the number of periods:\n"))
        loan_interest = float(input("Enter the loan interest:\n"))
        calculate_loan_principal(annuity_payment, periods, loan_interest)

def main():
    print("""What do you want to calculate?
    type "n" for number of monthly payments,
    type "a" for annuity monthly payment amount,
    type "p" for loan principal::""")
    check_input_options(input())

main()