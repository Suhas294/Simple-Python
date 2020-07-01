# Areas and perimeters of basic figures...........TEST CASE



print ("Enter the figure you want")
ch = input("Square,Rectangle,Circle: ")

if ch == 'Square':

s = float(input("Enter the value: "))
 Area_S = s*s
 Perimeter_S = 4*s
 print ("Area of Square: ",Area_S)
 print ("Perimeter of Square: ",Perimeter_S)

elif ch == 'Rectangle':

l = float(input("Enter the length: "))
b = float(input("Enter the breadth: "))
Area_R = l*b
Perimeter_R = 2*(l+b)
print ("Area of Rectangle: ",Area_R)
print ("Perimeter of Rectangle: ",Perimeter_R)

elif ch == 'Circle':
    
r = float(input("Enter the radius: ")
Area_C = 3.14*r*r
Perimeter_C = 2*3.14*r
print ("Area of Circle: ",Area_C)
print ("Perimeter of Circle: ",Perimeter_C)

else:
    print ("Wrong choice entered")


