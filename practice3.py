import math
a= int(input("Enter a"))
b= int(input("Enter b"))
c= int(input("Enter c"))
if(a==(math.sqrt(b**2 + c**2))):
    print("It is right triangle")
elif(b==(math.sqrt(a**2 + c**2))):
    print("It is right triangle")
elif(c==(math.sqrt(b**2 + a**2))):
    print("It is right triangle")
else:
    print("Not right triangle")    