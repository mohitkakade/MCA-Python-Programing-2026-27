seconds = int(input("Enter time duration in seconds: "))

hours = seconds // 3600
remaining = seconds % 3600

minutes = remaining // 60
seconds = remaining % 60

print("Hours =", hours)
print("Minutes =", minutes)
print("Seconds =", seconds)




Sample Output:
Enter time duration in seconds: 7385

Hours = 2
Minutes = 3
Seconds = 5
