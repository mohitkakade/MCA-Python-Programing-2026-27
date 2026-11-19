num = int(input("Enter an integer: "))

if num < 0:
    print("Not an Armstrong Number")

else:
    temp = num
    digits = len(str(num))
    total = 0

    while temp > 0:
        digit = temp % 10
        total = total + digit ** digits
        temp = temp // 10

    if total == num:
        print("Armstrong Number")
    else:
        print("Not an Armstrong Number")
