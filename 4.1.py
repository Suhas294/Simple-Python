# Area of the triangle having sides.....heron's formula

a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

# Semi Perimeter
s = (a + b + c) / 2
print("Semi Perimeter of the triangle is ", s)

#Area 

area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print("The area of the triangle is ", area)





