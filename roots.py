from math import sqrt

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))

d= b**2 - 4*a*c
if( d ==0):
    R1= R2 = -b/(2*a)
    print(R1,R2)
elif( d >0):
    R1= (-b + sqrt(d))/(2*a)
    R2= (-b - sqrt(d))/(2*a)
    print(R1,R2)
elif(d<0):
    real_part = -b / (2*a) 
    imaginary_part = sqrt(-d) / (2 * a)
    print(real_part , imaginary_part)





