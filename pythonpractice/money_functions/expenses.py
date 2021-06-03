import math
number_list = []
n = int(input("How many days did you eat out for lunch? "))

for i in range(1, n):
    print("Day",i)
    item = float(input("How much did you spend?"))
    print(item)
    number_list.append(item)

total = math.fsum(number_list)
print(f"\nYou spent {round(total,2)} on lunch this week")
