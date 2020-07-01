# Test Case for 1.1

num1 = float(input("Enter 1st number: "))
num2 = float(input("Enter 2nd number: "))

print("Enter the operation to perform")
ch = input("for specific operation like +,-,*,/,%: ")

result = 0
if ch == '+':
    result = num1 + num2
elif ch == '-':
    result = num1 - num2
elif ch == '*':
    result = num1 * num2
elif ch == '/':
    result = num1 / num2
elif ch == '%':
    reuslt = num1 % num2
else:
    print("Input symbol not recognized")

print(num1, ch, num2, ":", result)