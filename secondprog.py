import math

a = int(input("Enter the first side: "))
b = int(input("Enter the second side: "))
c = int(input("Enter the third side: "))

print("perimeter of triangle is: ", (a + b +c))

s = ((a + b +c)/2)

area = float ( math.sqrt(s*(s-a)*(s-b)*(s-c)))
print("area of triangle is: ", area)

x = a**2
y = b**2
z = c**2
print("First angle is: ", math.degrees(math.acos((y+z-x)/(2*b*c))))
print("second angle is: ", math.degrees(math.acos((x+z-y)/(2*a*c))))
print("third angle is: ", math.degrees(math.acos((x+y-z)/(2*a*b))))
