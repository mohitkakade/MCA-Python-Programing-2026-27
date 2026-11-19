units = int(input("Enter electricity units consumed: "))

if units <= 100:
    bill = units * 1.50

elif units <= 200:
    bill = (100 * 1.50) + (units - 100) * 2.50

elif units <= 300:
    bill = (100 * 1.50) + (100 * 2.50) + (units - 200) * 3.50

else:
    bill = (100 * 1.50) + (100 * 2.50) + (100 * 3.50) + (units - 300) * 5.00

print("Electricity Units =", units)
print("Total Electricity Bill = Rs.", bill)




Sample Output:
Enter electricity units consumed: 250

Electricity Units = 250
Total Electricity Bill = Rs. 550.0
