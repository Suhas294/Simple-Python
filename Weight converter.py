# Weight Converter

Weight = float(input("Enter the value: " ))

print("Enter the conversion u want")
ch = input("for operations like (K)g,(L)bs: ")

result = 0

if ch == '(K)g':
    result = Weight*2.20462
    print(result,"is the weight in (L)bs")

else:
    result = Weight/2.20462
    print(result,"is the weight in (K)g")


