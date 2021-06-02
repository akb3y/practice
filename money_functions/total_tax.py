service = input("Was your service: bad, okay, good, or great?  ").lower()

bill_total = float(input("How much was your bill including tax?  "))

if service == "bad":
    tip = 1
    print("Your total bill costs ", round(tip*bill_total))
elif service == "okay":
    tip = 1.15
    print("Your total bill costs ", round(tip*bill_total))
elif service == "good":
    tip = 1.18
    print("Your total bill costs ", round(tip*bill_total))
elif service == "great":
    tip = 1.2
    print("Your total bill costs ", round(tip*bill_total))
else: 
    print("Invalid Service")




