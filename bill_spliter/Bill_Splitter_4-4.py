import random 

print("Enter the number of friends joining (including you):")
num_friends = int(input())
friends_dict = {}

if num_friends <= 0:
    print("No one is joining for the party")
else:
    print("\nEnter the name of every friend (including you), each on a new line:")
    friends_dict = dict.fromkeys([input() for _ in range(num_friends)], 0)
    n_friends = len(friends_dict)
    friends = list(friends_dict.keys())
    lucky_friend = random.choice(friends)

    print("\nEnter the total bill value: ")
    bill = int(input())

    friends_dict = {k: round((bill / n_friends), 2) for (k, _) in friends_dict.items()}

    print('\nDo you want to use the "Who is lucky?" feature? Write Yes/No:')
    answer = input()
    if answer == 'Yes':
        print(f'\n{lucky_friend} is the lucky one!\n')
        friends_dict = {k: round(bill / (n_friends - 1), 2) for (k, _) in friends_dict.items()}
        friends_dict[lucky_friend] = 0
        print(friends_dict)
    else:
        print("\nNo one is going to be lucky\n")
        friends_dict = {k: round((bill / n_friends), 2) for (k, _) in friends_dict.items()}
        print(friends_dict)
