num = int(input("Enter an integer: "))

temp = abs(num)

count = 0
largest = 0
smallest = 9

if temp == 0:
    count = 1
    largest = 0
    smallest = 0

while temp > 0:
    digit = temp % 10

    count = count + 1

    if digit > largest:
        largest = digit

    if digit < smallest:
        smallest = digit

    temp = temp // 10

print("Number of Digits =", count)
print("Largest Digit =", largest)
print("Smallest Digit =", smallest)
