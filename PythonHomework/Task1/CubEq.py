print("There is an equation ax^3+bx^2+cx+d=0")
import math
a1=float(input("Input a"))
b1=float(input("Input b"))
c1=float(input("Input c"))
d1=float(input("Input d"))
a=b1/a1
b=c1/a1
c=d1/a1
Q=(a**2-3*b)/9
print(Q)
R=(2*a**3-9*a*b+27*c)/54
S=Q**3-R**2
print(S)
if S>0:
    y=(1/3)*math.acos(R/math.sqrt(Q**3))
    x1=-2*math.sqrt(Q)*math.cos(y)-a/3
    x2=-2*math.sqrt(Q)*math.cos(y+math.pi*2/3)-a/3
    x3=-2*math.sqrt(Q)*math.cos(y-math.pi*2/3)-a/3
    print(x1,", ", x2,", ", x3)
elif S<0:
    if Q>0:
        z=math.fabs(R)/Q**3
        y=(1/3)*math.log1p(z+math.sqrt(z**2-1))
        #как посчитать функцию sgn? нашел только через numpy
        import numpy as np
        x1=-2*np.sign(R)*math.sqrt(Q)*((math.exp(z)+math.exp(z))/2)-a/3
        print(x1, " and pair of complex roots")
    elif Q<0:
        z=math.fabs(R)/math.fabs(Q)**3
        y=(1/3)*math.log1p(z+math.sqrt(z**2+1))
        # аналогично
        import numpy as np
        x1=-2*np.sign(R)*math.sqrt(Q)*((math.exp(z)-math.exp(z))/2)-a/3
        print(x1, " and pair of complex roots")
    else:
        x1=-(c-a**3/27)**1/3-a/3
        print(x1, " and pair of complex roots")
else:
    x1=-2*R**(1/3)-a/3
    x2=R**(1/3)-a/3
    print(x1, ", x2=x3=", x2)