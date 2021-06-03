money_owed = float(input("How much do you owe on your loan? \n"))
apr = float(input("What is your annual percentage rate? \n"))
payment = float(input("What is you monthly payment? \n"))
months = int(input("How many months of payments do you want to see? \n"))

monthly_rate = apr/100/12

for i in range(months):
    interest_paid = money_owed * monthly_rate
    money_owed = money_owed + interest_paid

    if(money_owed-payment < 0):
        print(f'The last payment is {round( money_owed,2)}')
        print('You paid off the loan in', i+1, 'months')
        break
    money_owed = money_owed - payment

    print(f'Paid{round(payment,2)} of which {round(interest_paid,2)} was interest.', end=' ')
    print(f'\nNow I owe {round(money_owed,2)}')