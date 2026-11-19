num = int(input("Enter an integer: "))

if num == 0:
    print("Number is Zero")

elif num > 0:
    print("Number is Positive")

    if num % 2 == 0:
        print("Number is Even")
    else:
        print("Number is Odd")

else:
    print("Number is Negative")

    if num % 2 == 0:
        print("Number is Even")
    else:
        print("Number is Odd")
