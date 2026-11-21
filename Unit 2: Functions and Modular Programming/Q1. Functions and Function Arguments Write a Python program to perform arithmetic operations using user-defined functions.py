def add(a, b, operation="Addition"):
    return a + b

def subtract(a, b, operation="Subtraction"):
    return a - b

def multiply(a, b, operation="Multiplication"):
    return a * b

def divide(a, b, operation="Division"):
    if b != 0:
        return a / b
    return "Cannot divide by zero"

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

print("Addition:", add(n1, n2))
print("Subtraction:", subtract(a=n1, b=n2))
print("Multiplication:", multiply(a=n1, b=n2))
print("Division:", divide(a=n1, b=n2))


Enter first number: 20
Enter second number: 10
Addition: 30
Subtraction: 10
Multiplication: 200
Division: 2.0
