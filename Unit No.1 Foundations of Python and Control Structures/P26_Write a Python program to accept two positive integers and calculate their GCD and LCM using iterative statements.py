a = int(input("Enter first positive integer: "))
b = int(input("Enter second positive integer: "))

if a <= 0 or b <= 0:
    print("Enter positive integers")

else:
    x = a
    y = b

    while y != 0:
        temp = y
        y = x % y
        x = temp

    gcd = x
    lcm = (a * b) // gcd

    print("GCD =", gcd)
    print("LCM =", lcm)
