num = int(input("Enter an integer: "))

count = 0

if num <= 0:
    print("Enter a positive integer")

else:
    print("Factors are:")

    for i in range(1, num + 1):
        if num % i == 0:
            print(i)
            count = count + 1

    print("Total Factors =", count)
