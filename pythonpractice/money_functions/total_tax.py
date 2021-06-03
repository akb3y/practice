service = input("Was your service: bad, okay, good, or great?\n").lower()

bill_total = float(input("How much was your bill including tax?\n"))

if service == "bad":
    tip = 1
    total_tip = (tip - 1) * bill_total
    print("Your total bill costs: $", round(tip*bill_total,2), ", tax is = ", round(total_tip,2),sep='')
elif service == "okay":
    tip = 1.15
    total_tip = (tip - 1) * bill_total
    print("Your total bill costs: $", round(tip*bill_total,2), ", tax is = ", round(total_tip,2),sep='')
elif service == "good":
    tip = 1.18
    total_tip = (tip - 1) * bill_total
    print("Your total bill costs: $", round(tip*bill_total,2), ", tax is = ", round(total_tip,2),sep='')
elif service == "great":
    tip = 1.2
    total_tip = (tip - 1) * bill_total
    print("Your total bill costs: $", round(tip*bill_total,2), ", tax is = ", round(total_tip,2),sep='')
else: 
    print("Invalid Service")




