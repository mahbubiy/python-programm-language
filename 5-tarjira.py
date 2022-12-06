from math import*
x = int(input("x:"))
y = int(input("y:"))
z = int(input("z:"))
f = fabs(x**(y/x)-(y/x)**(1/3))+(y-x)*((cos(y)-z/(y-x))/(1+(y-x)**2))
print(f)
