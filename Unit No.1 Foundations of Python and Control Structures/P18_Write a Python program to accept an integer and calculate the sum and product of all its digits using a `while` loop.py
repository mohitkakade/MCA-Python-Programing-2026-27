num = int(input("Enter an integer: "))

temp = abs(num)
sum = 0
product = 1

if temp == 0:
    product = 0

while temp > 0:
    digit = temp % 10
    sum = sum + digit
    product = product * digit
    temp = temp // 10

print("Sum of Digits =", sum)
print("Product of Digits =", product)
