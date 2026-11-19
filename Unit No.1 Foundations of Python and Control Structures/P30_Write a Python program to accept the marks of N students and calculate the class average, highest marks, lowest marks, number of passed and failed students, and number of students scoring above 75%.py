n = int(input("Enter number of students: "))

if n <= 0:
    print("Invalid number of students")

else:
    total = 0
    highest = -1
    lowest = 101

    passed = 0
    failed = 0
    above75 = 0

    for i in range(1, n + 1):

        marks = float(input("Enter marks of student: "))

        total = total + marks

        if marks > highest:
            highest = marks

        if marks < lowest:
            lowest = marks

        if marks >= 40:
            passed = passed + 1
        else:
            failed = failed + 1

        if marks > 75:
            above75 = above75 + 1

    average = total / n

    print("\n----- CLASS RESULT -----")
    print("Class Average =", average)
    print("Highest Marks =", highest)
    print("Lowest Marks =", lowest)
    print("Number of Passed Students =", passed)
    print("Number of Failed Students =", failed)
    print("Students Scoring Above 75% =", above75)
