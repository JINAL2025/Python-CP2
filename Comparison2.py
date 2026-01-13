a = int (input("Enter the first integer : "))
b = int (input("Enter the second integer : "))
c = int (input("Enter the third integer : "))
if a>b :
    if a>c :
        print("The greatest integer is", a)
    else :
        print("The greatest integer is", c)
else :
    if b>c :
        print("The greatest integer is", b)
    else :
        print("The greatest integer is", c)
