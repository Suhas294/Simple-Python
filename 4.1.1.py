#TEST CASE FOR 4.1
# Areas of different triangles

print ("Enter the choice ")
ch = input("I,E,R: ")

if ch == 'I':
    b = float(input("Enter base: "))
    h = float(input("Enter height: "))
    Area_I = 0.5*b*h
    print ("Area of the triangle is ",Area_I)
    
    elif ch == 'E':
        a = float(input("Enter side: "))
        Area_E = 0.433*a*a
        print ("Area is ",Area_E)

        elif ch == 'R':
            s = float(input("Enter the base: "))
            p = float(input("Enter the perpendicular: "))
            Area_R = 0.5*s*p
            print ("Area of R is ",Area_R)

            else:
                print ("Wrong choice is entered")


