usage = float(input("Enter monthly data usage in GB: "))

if usage < 0:
    print("Invalid Usage")

elif usage <= 2:
    bill = 100

elif usage <= 5:
    bill = 100 + (usage - 2) * 50

else:
    bill = 100 + (3 * 50) + (usage - 5) * 30

if usage >= 0:
    print("Total Mobile Bill = Rs.", bill)
