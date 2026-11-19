while True:

    print("\n----- MATHEMATICAL MENU -----")
    print("1. Check Prime")
    print("2. Check Palindrome")
    print("3. Check Armstrong")
    print("4. Factorial")
    print("5. Fibonacci Series")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        num = int(input("Enter number: "))
        prime = True

        if num <= 1:
            prime = False

        else:
            for i in range(2, num):
                if num % i == 0:
                    prime = False
                    break

        if prime:
            print("Prime Number")
        else:
            print("Not a Prime Number")

    elif choice == 2:

        num = int(input("Enter number: "))
        temp = num
        reverse = 0

        if num >= 0:
            while temp > 0:
                digit = temp % 10
                reverse = reverse * 10 + digit
                temp = temp // 10

            if num == reverse:
                print("Palindrome Number")
            else:
                print("Not a Palindrome")

        else:
            print("Not a Palindrome")

    elif choice == 3:

        num = int(input("Enter number: "))

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

    elif choice == 4:

        num = int(input("Enter number: "))

        if num < 0:
            print("Factorial is not defined for negative numbers")

        else:
            fact = 1

            for i in range(1, num + 1):
                fact = fact * i

            print("Factorial =", fact)

    elif choice == 5:

        n = int(input("Enter number of terms: "))

        a = 0
        b = 1

        if n < 0:
            print("Enter a non-negative number")

        else:
            print("Fibonacci Series:")

            for i in range(n):
                print(a, end=" ")
                c = a + b
                a = b
                b = c

            print()

    elif choice == 6:

        print("Thank You!")
        break

    else:
        print("Invalid Choice")
