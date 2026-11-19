correct_pin = 1234
balance = 10000

pin = int(input("Enter ATM PIN: "))

if pin == correct_pin:

    amount = float(input("Enter withdrawal amount: "))

    if amount <= 0:
        print("Invalid Amount")

    elif amount > balance:
        print("Insufficient Balance")

    else:
        balance = balance - amount
        print("Withdrawal Successful")
        print("Remaining Balance =", balance)

else:
    print("Incorrect PIN")
