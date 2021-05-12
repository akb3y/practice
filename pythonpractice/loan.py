money_owed = float(input("How much do you owe? \n"))
apr = float(input("What is your annual percentage rate? \n"))
payment = float(input("WWhat is you monthly payment? \n"))
months = int(input("How many months do you want to see? \n"))

monthly_rate = apr/100/12

for i in range(months):
    interest_paid = money_owed * monthly_rate
    money_owed = round(money_owed + interest_paid,2)

    if(money_owed-payment < 0):
        print('The last payment is', money_owed)
        print('You paid off the loan in', i+1, 'months')
        break 

    money_owed = money_owed - payment

    print('Paid', payment, 'of which', interest_paid, 'was interest.', end=' ')
    print('\nNow I owe', money_owed)